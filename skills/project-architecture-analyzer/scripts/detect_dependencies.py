#!/usr/bin/env python3
"""
Dependency Detector - Analyze module dependencies and relationships
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class ModuleInfo:
    name: str
    path: str
    imports: List[str] = field(default_factory=list)
    imported_by: List[str] = field(default_factory=list)
    loc: int = 0
    type: str = "module"


class DependencyDetector:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.modules: Dict[str, ModuleInfo] = {}
        self.dependency_graph: Dict[str, List[str]] = defaultdict(list)
        self.reverse_graph: Dict[str, List[str]] = defaultdict(list)
        self.circular_dependencies: List[Tuple[str, str]] = []
        self.coupling_metrics: Dict[str, Any] = {}
    
    def analyze(self) -> Dict[str, Any]:
        self._scan_modules()
        self._build_dependency_graph()
        self._detect_circular_dependencies()
        self._calculate_coupling_metrics()
        return self._generate_report()
    
    def _scan_modules(self):
        extensions = {
            '.js': self._parse_js_imports,
            '.ts': self._parse_js_imports,
            '.jsx': self._parse_js_imports,
            '.tsx': self._parse_js_imports,
            '.py': self._parse_python_imports,
            '.go': self._parse_go_imports,
            '.java': self._parse_java_imports
        }
        
        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if d not in [
                'node_modules', '.git', '__pycache__', 'venv', 'dist', 
                'build', '.next', 'target', 'vendor', 'pkg'
            ]]
            
            for file in files:
                ext = Path(file).suffix.lower()
                if ext in extensions:
                    file_path = Path(root) / file
                    rel_path = file_path.relative_to(self.project_path)
                    module_name = str(rel_path).replace('\\', '/')
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        imports = extensions[ext](content, rel_path)
                        loc = len([l for l in content.split('\n') if l.strip() and not l.strip().startswith(('#', '//', '/*'))])
                        
                        module_type = self._determine_module_type(rel_path, content)
                        
                        self.modules[module_name] = ModuleInfo(
                            name=module_name,
                            path=str(file_path),
                            imports=imports,
                            loc=loc,
                            type=module_type
                        )
                    except IOError:
                        pass
    
    def _parse_js_imports(self, content: str, file_path: Path) -> List[str]:
        imports = []
        
        patterns = [
            r'import\s+.*?from\s+[\'"]([^\'"]+)[\'"]',
            r'import\s+[\'"]([^\'"]+)[\'"]',
            r'require\s*\(\s*[\'"]([^\'"]+)[\'"]\s*\)',
            r'import\s*\(\s*[\'"]([^\'"]+)[\'"]\s*\)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content)
            imports.extend(matches)
        
        return list(set(imports))
    
    def _parse_python_imports(self, content: str, file_path: Path) -> List[str]:
        imports = []
        
        patterns = [
            r'^import\s+([a-zA-Z0-9_.]+)',
            r'^from\s+([a-zA-Z0-9_.]+)\s+import',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content, re.MULTILINE)
            imports.extend(matches)
        
        return list(set(imports))
    
    def _parse_go_imports(self, content: str, file_path: Path) -> List[str]:
        imports = []
        
        single_import = r'import\s+[\'"]([^\'"]+)[\'"]'
        multi_import = r'import\s*\(([\s\S]*?)\)'
        
        imports.extend(re.findall(single_import, content))
        
        for match in re.findall(multi_import, content):
            for line in match.split('\n'):
                line = line.strip()
                if line and not line.startswith('//'):
                    imp = re.search(r'[\'"]([^\'"]+)[\'"]', line)
                    if imp:
                        imports.append(imp.group(1))
        
        return list(set(imports))
    
    def _parse_java_imports(self, content: str, file_path: Path) -> List[str]:
        imports = []
        pattern = r'import\s+([a-zA-Z0-9_.]+);'
        imports.extend(re.findall(pattern, content))
        return list(set(imports))
    
    def _determine_module_type(self, rel_path: Path, content: str) -> str:
        path_str = str(rel_path).lower()
        
        if 'test' in path_str or 'spec' in path_str:
            return "test"
        if 'util' in path_str or 'helper' in path_str or 'lib' in path_str:
            return "utility"
        if 'component' in path_str:
            return "component"
        if 'service' in path_str:
            return "service"
        if 'controller' in path_str or 'route' in path_str:
            return "controller"
        if 'model' in path_str or 'entity' in path_str:
            return "model"
        if 'view' in path_str:
            return "view"
        if 'config' in path_str or 'setting' in path_str:
            return "config"
        if rel_path.name in ['index.js', 'index.ts', 'main.py', 'app.py', 'main.go', 'main.java']:
            return "entry"
        
        return "module"
    
    def _build_dependency_graph(self):
        for module_name, module_info in self.modules.items():
            for imp in module_info.imports:
                resolved = self._resolve_import(imp, module_name)
                if resolved and resolved in self.modules:
                    self.dependency_graph[module_name].append(resolved)
                    self.reverse_graph[resolved].append(module_name)
    
    def _resolve_import(self, import_path: str, from_module: str) -> str:
        if import_path.startswith('.'):
            from_dir = str(Path(from_module).parent)
            if from_dir == '.':
                from_dir = ''
            
            parts = import_path.split('/')
            current = from_dir.split('/') if from_dir else []
            
            for part in parts:
                if part == '..':
                    if current:
                        current.pop()
                elif part != '.':
                    current.append(part)
            
            resolved = '/'.join(current)
            
            for ext in ['.js', '.ts', '.jsx', '.tsx', '.py', '.go']:
                test_path = resolved + ext
                if test_path in self.modules:
                    return test_path
            
            index_path = resolved + '/index.js'
            if index_path in self.modules:
                return index_path
        
        for module in self.modules:
            if import_path in module or module.endswith(import_path.replace('/', os.sep) + '.py'):
                return module
        
        return None
    
    def _detect_circular_dependencies(self):
        visited = set()
        rec_stack = set()
        
        def dfs(node: str, path: List[str]) -> bool:
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in self.dependency_graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor, path + [neighbor]):
                        return True
                elif neighbor in rec_stack:
                    cycle_start = path.index(neighbor) if neighbor in path else len(path) - 1
                    cycle = path[cycle_start:] + [neighbor, node]
                    if len(cycle) >= 2:
                        self.circular_dependencies.append((node, neighbor))
                    return True
            
            rec_stack.remove(node)
            return False
        
        for module in self.modules:
            if module not in visited:
                dfs(module, [module])
    
    def _calculate_coupling_metrics(self):
        afferent_coupling = {}
        efferent_coupling = {}
        instability = {}
        
        for module in self.modules:
            ca = len(self.reverse_graph.get(module, []))
            ce = len(self.dependency_graph.get(module, []))
            
            afferent_coupling[module] = ca
            efferent_coupling[module] = ce
            
            total = ca + ce
            instability[module] = ce / total if total > 0 else 0
        
        self.coupling_metrics = {
            "afferent_coupling": afferent_coupling,
            "efferent_coupling": efferent_coupling,
            "instability": instability,
            "avg_instability": sum(instability.values()) / len(instability) if instability else 0,
            "high_coupling_modules": [
                m for m, i in instability.items() 
                if i > 0.7 or i < 0.3
            ]
        }
    
    def _generate_report(self) -> Dict[str, Any]:
        module_summary = {}
        for name, info in self.modules.items():
            module_summary[name] = {
                "type": info.type,
                "loc": info.loc,
                "imports_count": len(info.imports),
                "imported_by_count": len(self.reverse_graph.get(name, []))
            }
        
        entry_modules = [m for m, info in self.modules.items() if info.type == "entry"]
        core_modules = [m for m, info in self.modules.items() if info.type in ["service", "model", "controller"]]
        utility_modules = [m for m, info in self.modules.items() if info.type == "utility"]
        
        return {
            "summary": {
                "total_modules": len(self.modules),
                "total_loc": sum(m.loc for m in self.modules.values()),
                "circular_dependencies_count": len(self.circular_dependencies),
                "avg_instability": round(self.coupling_metrics["avg_instability"], 3)
            },
            "module_types": {
                "entry": entry_modules,
                "core": core_modules,
                "utility": utility_modules
            },
            "modules": module_summary,
            "dependency_graph": dict(self.dependency_graph),
            "circular_dependencies": self.circular_dependencies,
            "coupling_metrics": {
                "avg_instability": round(self.coupling_metrics["avg_instability"], 3),
                "high_coupling_modules": self.coupling_metrics["high_coupling_modules"][:10]
            },
            "top_imported_modules": sorted(
                [(m, len(v)) for m, v in self.reverse_graph.items()],
                key=lambda x: x[1],
                reverse=True
            )[:10]
        }


def detect_dependencies(project_path: str) -> Dict[str, Any]:
    detector = DependencyDetector(project_path)
    return detector.analyze()


def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python detect_dependencies.py <project_path>")
        sys.exit(1)
    
    project_path = sys.argv[1]
    results = detect_dependencies(project_path)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
