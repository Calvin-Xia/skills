#!/usr/bin/env python3
"""
Tech Stack Analyzer - Automatically detect project technology stack
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Any


class TechStackAnalyzer:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.results = {
            "project_type": "unknown",
            "languages": {},
            "frameworks": {"frontend": [], "backend": []},
            "databases": [],
            "build_tools": [],
            "devops": [],
            "dependencies": {},
            "version_info": {}
        }
    
    def analyze(self) -> Dict[str, Any]:
        self._detect_languages()
        self._detect_package_managers()
        self._detect_frameworks()
        self._detect_databases()
        self._detect_devops()
        self._determine_project_type()
        return self.results
    
    def _detect_languages(self):
        extensions = {
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.jsx': 'JavaScript (JSX)',
            '.tsx': 'TypeScript (TSX)',
            '.py': 'Python',
            '.java': 'Java',
            '.go': 'Go',
            '.rs': 'Rust',
            '.rb': 'Ruby',
            '.php': 'PHP',
            '.cs': 'C#',
            '.cpp': 'C++',
            '.c': 'C',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.vue': 'Vue',
            '.html': 'HTML',
            '.css': 'CSS',
            '.scss': 'SCSS',
            '.less': 'Less'
        }
        
        lang_counts = {}
        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', '__pycache__', 'venv', 'dist', 'build', '.next', 'target']]
            
            for file in files:
                ext = Path(file).suffix.lower()
                if ext in extensions:
                    lang = extensions[ext]
                    lang_counts[lang] = lang_counts.get(lang, 0) + 1
        
        total = sum(lang_counts.values()) if lang_counts else 0
        if total > 0:
            self.results["languages"] = {
                lang: {"files": count, "percentage": round(count / total * 100, 1)}
                for lang, count in sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)
            }
    
    def _detect_package_managers(self):
        package_files = {
            'package.json': 'npm/yarn/pnpm',
            'yarn.lock': 'Yarn',
            'pnpm-lock.yaml': 'pnpm',
            'package-lock.json': 'npm',
            'requirements.txt': 'pip',
            'pyproject.toml': 'Poetry/pip',
            'Pipfile': 'Pipenv',
            'poetry.lock': 'Poetry',
            'go.mod': 'Go modules',
            'go.sum': 'Go modules',
            'pom.xml': 'Maven',
            'build.gradle': 'Gradle',
            'build.gradle.kts': 'Gradle (Kotlin DSL)',
            'Cargo.toml': 'Cargo',
            'Cargo.lock': 'Cargo',
            'composer.json': 'Composer',
            'Gemfile': 'Bundler',
            'Gemfile.lock': 'Bundler'
        }
        
        for file, manager in package_files.items():
            if (self.project_path / file).exists():
                if manager not in self.results["build_tools"]:
                    self.results["build_tools"].append(manager)
                
                if file == 'package.json':
                    self._parse_package_json()
                elif file == 'requirements.txt':
                    self._parse_requirements_txt()
                elif file == 'go.mod':
                    self._parse_go_mod()
    
    def _parse_package_json(self):
        pkg_path = self.project_path / 'package.json'
        if not pkg_path.exists():
            return
        
        try:
            with open(pkg_path, 'r', encoding='utf-8') as f:
                pkg = json.load(f)
            
            deps = {}
            for dep_type in ['dependencies', 'devDependencies', 'peerDependencies']:
                if dep_type in pkg:
                    deps[dep_type] = pkg[dep_type]
            
            self.results["dependencies"]["npm"] = deps
            
            if 'version' in pkg:
                self.results["version_info"]["package"] = pkg['version']
            
            all_deps = {**deps.get('dependencies', {}), **deps.get('devDependencies', {})}
            
            frontend_frameworks = {
                'react': 'React',
                'vue': 'Vue',
                'angular': 'Angular',
                '@angular/core': 'Angular',
                'svelte': 'Svelte',
                'next': 'Next.js',
                'nuxt': 'Nuxt.js',
                'gatsby': 'Gatsby',
                'vite': 'Vite',
                'webpack': 'Webpack',
                'tailwindcss': 'Tailwind CSS',
                '@emotion/react': 'Emotion',
                'styled-components': 'Styled Components'
            }
            
            backend_frameworks = {
                'express': 'Express',
                'fastify': 'Fastify',
                '@nestjs/core': 'NestJS',
                'koa': 'Koa',
                'hono': 'Hono',
                'axios': 'Axios'
            }
            
            for dep, name in frontend_frameworks.items():
                if dep in all_deps:
                    if name not in self.results["frameworks"]["frontend"]:
                        self.results["frameworks"]["frontend"].append(name)
            
            for dep, name in backend_frameworks.items():
                if dep in all_deps:
                    if name not in self.results["frameworks"]["backend"]:
                        self.results["frameworks"]["backend"].append(name)
                        
        except (json.JSONDecodeError, IOError):
            pass
    
    def _parse_requirements_txt(self):
        req_path = self.project_path / 'requirements.txt'
        if not req_path.exists():
            return
        
        try:
            with open(req_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            deps = {}
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    match = re.match(r'^([a-zA-Z0-9_-]+)', line)
                    if match:
                        pkg = match.group(1)
                        deps[pkg] = line
            
            self.results["dependencies"]["pip"] = deps
            
            python_frameworks = {
                'django': 'Django',
                'flask': 'Flask',
                'fastapi': 'FastAPI',
                'tornado': 'Tornado',
                'sanic': 'Sanic',
                'aiohttp': 'AIOHTTP',
                'starlette': 'Starlette'
            }
            
            for pkg, name in python_frameworks.items():
                if pkg in deps:
                    if name not in self.results["frameworks"]["backend"]:
                        self.results["frameworks"]["backend"].append(name)
                        
        except IOError:
            pass
    
    def _parse_go_mod(self):
        mod_path = self.project_path / 'go.mod'
        if not mod_path.exists():
            return
        
        try:
            with open(mod_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            module_match = re.search(r'module\s+(\S+)', content)
            if module_match:
                self.results["version_info"]["module"] = module_match.group(1)
            
            go_match = re.search(r'go\s+(\d+\.\d+)', content)
            if go_match:
                self.results["version_info"]["go"] = go_match.group(1)
            
            go_frameworks = {
                'github.com/gin-gonic/gin': 'Gin',
                'github.com/labstack/echo': 'Echo',
                'github.com/gofiber/fiber': 'Fiber',
                'github.com/go-chi/chi': 'Chi',
                'github.com/gorilla/mux': 'Gorilla Mux'
            }
            
            for pkg, name in go_frameworks.items():
                if pkg in content:
                    if name not in self.results["frameworks"]["backend"]:
                        self.results["frameworks"]["backend"].append(name)
                        
        except IOError:
            pass
    
    def _detect_frameworks(self):
        indicator_files = {
            'vue.config.js': 'Vue',
            'vite.config.js': 'Vite',
            'vite.config.ts': 'Vite',
            'angular.json': 'Angular',
            'next.config.js': 'Next.js',
            'next.config.mjs': 'Next.js',
            'nuxt.config.js': 'Nuxt.js',
            'nuxt.config.ts': 'Nuxt.js',
            'gatsby-config.js': 'Gatsby',
            'svelte.config.js': 'Svelte',
            'tailwind.config.js': 'Tailwind CSS',
            'tailwind.config.ts': 'Tailwind CSS'
        }
        
        for file, framework in indicator_files.items():
            if (self.project_path / file).exists():
                if framework in ['Vue', 'Svelte']:
                    if framework not in self.results["frameworks"]["frontend"]:
                        self.results["frameworks"]["frontend"].append(framework)
                elif framework == 'Tailwind CSS':
                    if 'Tailwind CSS' not in self.results["frameworks"]["frontend"]:
                        self.results["frameworks"]["frontend"].append('Tailwind CSS')
                else:
                    if framework not in self.results["build_tools"]:
                        self.results["build_tools"].append(framework)
        
        if (self.project_path / 'manage.py').exists():
            if 'Django' not in self.results["frameworks"]["backend"]:
                self.results["frameworks"]["backend"].append('Django')
        
        if 'Django' not in self.results["frameworks"]["backend"]:
            self._check_django_in_deps()
        
        if (self.project_path / 'main.py').exists() or (self.project_path / 'app.py').exists():
            content = ""
            for fname in ['main.py', 'app.py']:
                fpath = self.project_path / fname
                if fpath.exists():
                    try:
                        with open(fpath, 'r', encoding='utf-8') as f:
                            content += f.read()
                    except IOError:
                        pass
            
            if 'FastAPI' in content and 'FastAPI' not in self.results["frameworks"]["backend"]:
                self.results["frameworks"]["backend"].append('FastAPI')
            if 'Flask' in content and 'Flask' not in self.results["frameworks"]["backend"]:
                self.results["frameworks"]["backend"].append('Flask')
    def _check_django_in_deps(self):
        req_path = self.project_path / 'requirements.txt'
        if req_path.exists():
            try:
                content = req_path.read_text(encoding='utf-8', errors='ignore')
                if re.search(r'^[Dd]jango\b', content, re.MULTILINE):
                    self.results["frameworks"]["backend"].append('Django')
                    return
            except IOError:
                pass
        
        toml_path = self.project_path / 'pyproject.toml'
        if toml_path.exists():
            try:
                content = toml_path.read_text(encoding='utf-8', errors='ignore')
                if re.search(r'[Dd]jango', content):
                    self.results["frameworks"]["backend"].append('Django')
                    return
            except IOError:
                pass
        
        if (self.project_path / 'settings.py').exists():
            self.results["frameworks"]["backend"].append('Django')
    
    def _detect_databases(self):
        db_indicators = {
            'postgresql': ['psycopg2', 'pg', 'postgres', 'pg-promise'],
            'mysql': ['mysql2', 'mysql-connector', 'pymysql', 'mysql'],
            'mongodb': ['mongoose', 'pymongo', 'mongodb'],
            'redis': ['redis', 'ioredis'],
            'sqlite': ['sqlite3', 'better-sqlite3'],
            'elasticsearch': ['elasticsearch', '@elastic/elasticsearch'],
            'prisma': ['prisma', '@prisma/client']
        }
        
        all_deps = {}
        for manager_deps in self.results["dependencies"].values():
            if isinstance(manager_deps, dict):
                for dep_type in ['dependencies', 'devDependencies']:
                    if dep_type in manager_deps:
                        all_deps.update(manager_deps[dep_type])
                all_deps.update(manager_deps)
        
        for db, indicators in db_indicators.items():
            for indicator in indicators:
                if indicator in all_deps:
                    if db not in self.results["databases"]:
                        self.results["databases"].append(db)
                    break
        
        db_files = {
            'prisma/schema.prisma': 'Prisma',
            'db.sqlite3': 'SQLite',
            'database.db': 'SQLite'
        }
        
        for file, db in db_files.items():
            if (self.project_path / file).exists():
                if db not in self.results["databases"]:
                    self.results["databases"].append(db)
    
    def _detect_devops(self):
        devops_indicators = {
            '.github/workflows': 'GitHub Actions',
            '.gitlab-ci.yml': 'GitLab CI',
            'Jenkinsfile': 'Jenkins',
            '.circleci/config.yml': 'CircleCI',
            'Dockerfile': 'Docker',
            'docker-compose.yml': 'Docker Compose',
            'docker-compose.yaml': 'Docker Compose',
            'kubernetes': 'Kubernetes',
            'k8s': 'Kubernetes',
            'helm': 'Helm',
            'terraform': 'Terraform',
            '.terraform': 'Terraform',
            'Pulumi.yaml': 'Pulumi'
        }
        
        for indicator, tool in devops_indicators.items():
            path = self.project_path / indicator
            if path.exists() and (path.is_file() or path.is_dir()):
                if tool not in self.results["devops"]:
                    self.results["devops"].append(tool)
    
    def _determine_project_type(self):
        frameworks = self.results["frameworks"]
        languages = self.results["languages"]
        
        has_frontend = len(frameworks["frontend"]) > 0
        has_backend = len(frameworks["backend"]) > 0
        
        if has_frontend and has_backend:
            self.results["project_type"] = "fullstack"
        elif has_frontend:
            self.results["project_type"] = "frontend"
        elif has_backend:
            self.results["project_type"] = "backend"
        elif "HTML" in languages:
            self.results["project_type"] = "static_site"
        elif "Python" in languages and any(
            lib in str(self.results["dependencies"]) 
            for lib in ["pandas", "numpy", "scikit", "tensorflow", "torch"]
        ):
            self.results["project_type"] = "data_science"
        elif any(lang in languages for lang in ["Java", "C#", "Go"]):
            self.results["project_type"] = "backend"
        else:
            self.results["project_type"] = "library"


def analyze_tech_stack(project_path: str) -> Dict[str, Any]:
    analyzer = TechStackAnalyzer(project_path)
    return analyzer.analyze()


def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python analyze_tech_stack.py <project_path>")
        sys.exit(1)
    
    project_path = sys.argv[1]
    results = analyze_tech_stack(project_path)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
