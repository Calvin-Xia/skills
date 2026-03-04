#!/usr/bin/env python3
"""
Report Generator - Generate structured architecture analysis reports
"""

import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path


class ReportGenerator:
    def __init__(self, tech_stack: Dict[str, Any], dependencies: Dict[str, Any]):
        self.tech_stack = tech_stack
        self.dependencies = dependencies
        self.issues = {"P0": [], "P1": [], "P2": [], "P3": []}
    
    def generate(self, project_name: str = "Project") -> str:
        self._analyze_issues()
        return self._format_report(project_name)
    
    def _analyze_issues(self):
        if self.dependencies.get("circular_dependencies"):
            for cycle in self.dependencies["circular_dependencies"][:5]:
                self.issues["P1"].append({
                    "type": "circular_dependency",
                    "description": f"Circular dependency detected: {cycle[0]} <-> {cycle[1]}",
                    "recommendation": "Consider refactoring to break the circular dependency"
                })
        
        coupling = self.dependencies.get("coupling_metrics", {})
        if coupling.get("avg_instability", 0) > 0.8:
            self.issues["P2"].append({
                "type": "high_coupling",
                "description": f"High average instability: {coupling['avg_instability']:.2f}",
                "recommendation": "Review module dependencies and consider introducing interfaces"
            })
        
        for module in coupling.get("high_coupling_modules", [])[:5]:
            self.issues["P2"].append({
                "type": "unstable_module",
                "description": f"Module with extreme coupling: {module}",
                "recommendation": "Evaluate if this module should be split or consolidated"
            })
        
        lang_count = len(self.tech_stack.get("languages", {}))
        if lang_count > 5:
            self.issues["P2"].append({
                "type": "polyglot",
                "description": f"Multiple languages detected: {lang_count}",
                "recommendation": "Consider standardizing on fewer languages for maintainability"
            })
        
        if not self.tech_stack.get("devops"):
            self.issues["P3"].append({
                "type": "no_devops",
                "description": "No DevOps tooling detected",
                "recommendation": "Consider adding CI/CD pipeline and containerization"
            })
        
        if not self.tech_stack.get("databases"):
            self.issues["P3"].append({
                "type": "no_database",
                "description": "No database detected",
                "recommendation": "Verify if data persistence is needed"
            })
    
    def _format_report(self, project_name: str) -> str:
        report = []
        report.append(f"# 项目架构分析报告")
        report.append(f"\n**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**项目名称**: {project_name}")
        
        report.append("\n---\n")
        report.append("## 执行摘要\n")
        
        project_type = self.tech_stack.get("project_type", "unknown")
        type_map = {
            "fullstack": "全栈应用",
            "frontend": "前端应用",
            "backend": "后端服务",
            "static_site": "静态网站",
            "data_science": "数据科学项目",
            "library": "库/工具"
        }
        report.append(f"- **项目类型**: {type_map.get(project_type, project_type)}")
        
        langs = self.tech_stack.get("languages", {})
        if langs:
            top_langs = list(langs.keys())[:3]
            report.append(f"- **主要语言**: {', '.join(top_langs)}")
        
        frameworks = self.tech_stack.get("frameworks", {})
        all_frameworks = frameworks.get("frontend", []) + frameworks.get("backend", [])
        if all_frameworks:
            report.append(f"- **框架**: {', '.join(all_frameworks[:5])}")
        
        health_score = self._calculate_health_score()
        health_map = {4: "优秀", 3: "良好", 2: "一般", 1: "需改进"}
        report.append(f"- **整体健康度**: {health_map.get(health_score, '未知')}")
        
        report.append("\n---\n")
        report.append("## 技术栈分析\n")
        
        report.append("### 语言分布\n")
        if langs:
            report.append("| 语言 | 文件数 | 占比 |")
            report.append("|------|--------|------|")
            for lang, info in list(langs.items())[:10]:
                report.append(f"| {lang} | {info['files']} | {info['percentage']}% |")
        else:
            report.append("未能检测到编程语言")
        
        report.append("\n### 框架\n")
        if frameworks.get("frontend"):
            report.append(f"**前端**: {', '.join(frameworks['frontend'])}")
        if frameworks.get("backend"):
            report.append(f"**后端**: {', '.join(frameworks['backend'])}")
        
        databases = self.tech_stack.get("databases", [])
        if databases:
            report.append(f"\n### 数据库\n{', '.join(databases)}")
        
        devops = self.tech_stack.get("devops", [])
        if devops:
            report.append(f"\n### DevOps\n{', '.join(devops)}")
        
        report.append("\n---\n")
        report.append("## 模块架构\n")
        
        dep_summary = self.dependencies.get("summary", {})
        report.append(f"- **总模块数**: {dep_summary.get('total_modules', 0)}")
        report.append(f"- **总代码行数**: {dep_summary.get('total_loc', 0):,}")
        report.append(f"- **循环依赖数**: {dep_summary.get('circular_dependencies_count', 0)}")
        
        module_types = self.dependencies.get("module_types", {})
        if module_types.get("entry"):
            report.append(f"\n**入口模块**: {', '.join(module_types['entry'][:5])}")
        if module_types.get("core"):
            report.append(f"\n**核心模块**: {len(module_types['core'])} 个")
        if module_types.get("utility"):
            report.append(f"\n**工具模块**: {len(module_types['utility'])} 个")
        
        top_imported = self.dependencies.get("top_imported_modules", [])
        if top_imported:
            report.append("\n### 最常被引用的模块\n")
            report.append("| 模块 | 被引用次数 |")
            report.append("|------|------------|")
            for module, count in top_imported[:5]:
                report.append(f"| {module} | {count} |")
        
        report.append("\n---\n")
        report.append("## 问题与风险\n")
        
        for priority in ["P0", "P1", "P2", "P3"]:
            issues = self.issues.get(priority, [])
            if issues:
                priority_names = {"P0": "紧急", "P1": "高优先级", "P2": "中优先级", "P3": "低优先级"}
                report.append(f"\n### {priority} - {priority_names[priority]}\n")
                for i, issue in enumerate(issues, 1):
                    report.append(f"{i}. **{issue['type']}**: {issue['description']}")
                    report.append(f"   - 建议: {issue['recommendation']}")
        
        if not any(self.issues.values()):
            report.append("\n未检测到明显问题 ✓")
        
        report.append("\n---\n")
        report.append("## 改进建议\n")
        report.append(self._generate_recommendations())
        
        return "\n".join(report)
    
    def _calculate_health_score(self) -> int:
        score = 4
        
        if self.dependencies.get("circular_dependencies"):
            score -= 1
        
        coupling = self.dependencies.get("coupling_metrics", {})
        if coupling.get("avg_instability", 0) > 0.8:
            score -= 1
        
        if len(self.issues["P0"]) > 0 or len(self.issues["P1"]) > 2:
            score -= 1
        
        return max(1, score)
    
    def _generate_recommendations(self) -> str:
        recommendations = []
        
        if self.dependencies.get("circular_dependencies"):
            recommendations.append("1. **解决循环依赖**: 重构模块结构，引入接口或事件机制解耦")
        
        if not self.tech_stack.get("devops"):
            recommendations.append("2. **建立CI/CD流程**: 添加自动化测试和部署流程")
        
        coupling = self.dependencies.get("coupling_metrics", {})
        if coupling.get("avg_instability", 0) > 0.7:
            recommendations.append("3. **降低模块耦合**: 考虑引入依赖注入或接口抽象")
        
        if not recommendations:
            recommendations.append("1. **持续监控**: 定期进行架构审查，保持代码质量")
            recommendations.append("2. **文档完善**: 补充架构设计文档和API文档")
        
        return "\n".join(recommendations)


def generate_report(tech_stack: Dict[str, Any], dependencies: Dict[str, Any], project_name: str = "Project") -> str:
    generator = ReportGenerator(tech_stack, dependencies)
    return generator.generate(project_name)


def main():
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python generate_report.py <tech_stack.json> <dependencies.json> [project_name]")
        sys.exit(1)
    
    tech_stack_path = sys.argv[1]
    dependencies_path = sys.argv[2]
    project_name = sys.argv[3] if len(sys.argv) > 3 else "Project"
    
    with open(tech_stack_path, 'r', encoding='utf-8') as f:
        tech_stack = json.load(f)
    
    with open(dependencies_path, 'r', encoding='utf-8') as f:
        dependencies = json.load(f)
    
    report = generate_report(tech_stack, dependencies, project_name)
    print(report)


if __name__ == "__main__":
    main()
