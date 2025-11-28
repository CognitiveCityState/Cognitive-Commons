import re
import os
import json
from typing import List, Dict, Optional, Any
from dashscope import Generation
import dashscope
from datetime import datetime

# AI-Assisted Generation (DeepSeek, Doubao) | Manually Reviewed and Modified by Author
# Project: Recursive Adversarial Meta-Thinking Network | License: Apache 2.0

# Set API base URL
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'


# ===================== Core Framework for Personal Strategic Decision System =====================
class StrategicDecisionFramework:
    """
    Core Framework for Personal Strategic Decision System
    - Provides reference for constructors, critics, and observers
    - Supports both framework extraction and implantation modes
    - Contains six strategic analysis dimensions for comprehensive decision support
    """

    def __init__(self):
        """Initialize the strategic framework with six core analytical dimensions"""
        self.frameworks = {
            "three_dimensional_matrix": self._get_3d_matrix(),
            "three_level_classification": self._get_3level_classification(),
            "dynamic_stability": self._get_dynamic_stability(),
            "option_management": self._get_option_management(),
            "sequential_progressive": self._get_sequential_progressive(),
            "hub_ecological_niche": self._get_hub_ecological_niche()
        }
        self.extracted_framework = None  # Store user-extracted strategic system

    def _get_3d_matrix(self) -> Dict[str, Any]:
        """Three-Dimensional Matrix - Ecological Niche Positioning Compass"""
        return {
            "name": "Three-Dimensional Matrix",
            "description": "Strategic analysis tool for self-positioning and opportunity assessment in any environment",
            "dimensions": {
                "trait": {
                    "name": "Trait Dimension",
                    "description": "Core competencies and innate tendencies",
                    "analysis_questions": [
                        "What is the user good at? Not good at?",
                        "What is the user's core competency pattern?",
                        "What are the user's intrinsic motivations and values?"
                    ]
                },
                "path": {
                    "name": "Path Dimension",
                    "description": "Specific ways to realize value, combining and applying traits",
                    "analysis_questions": [
                        "How does the user create value?",
                        "Which path maximizes the user's advantages?",
                        "What are the synergistic effects of different competency combinations?"
                    ]
                },
                "space": {
                    "name": "Space Dimension",
                    "description": "The battlefield where traits and paths apply and its rules",
                    "analysis_questions": [
                        "Is the chosen field a blue ocean or red ocean?",
                        "What are the rules and barriers in this space?",
                        "Can user advantages be maximized in this space?"
                    ]
                }
            },
            "application_guidance": "When facing new opportunities, use the 3D matrix to quickly assess compatibility, ensuring path choices align with core traits"
        }

    def _get_3level_classification(self) -> Dict[str, Any]:
        """Three-Level Classification - Organizational System Deconstruction Microscope"""
        return {
            "name": "Three-Level Classification",
            "description": "Tool to penetrate organizational appearances and understand internal power structures, value orientations, and capability distributions",
            "levels": {
                "level1": {
                    "name": "Value Orientation",
                    "categories": {
                        "industry": "Industry - Profit and growth driven, focusing on practice and results",
                        "academia": "Academia - Knowledge and influence driven, focusing on theory and innovation"
                    }
                },
                "level2": {
                    "name": "Organizational Form",
                    "categories": {
                        "private": "Private Enterprise - Profit driven, primarily dynamic stability, high salary and growth ceiling",
                        "state_owned": "State-Owned Enterprise - Balance between order and profit, between dynamic and static stability",
                        "government": "Government - Order and governance driven, primarily static stability"
                    }
                },
                "level3": {
                    "name": "Capability Mode",
                    "categories": {
                        "strategy": "Strategic Side - Defining problems, planning directions, integrating resources, building rules (Why & What)",
                        "execution": "Execution Side - Solving problems, completing tasks, implementing functions, optimizing experiences (How)"
                    }
                }
            },
            "application_guidance": "When job hunting or collaborating, precisely analyze the core operations and compatibility of target organizations or departments"
        }

    def _get_dynamic_stability(self) -> Dict[str, Any]:
        """Dynamic Stability Theory - Personal Development Anchor"""
        return {
            "name": "Dynamic Stability Theory",
            "description": "Core values and ultimate decision-making criteria for all choices",
            "core_principles": {
                "philosophy": "True stability should not be 'static stability' dependent on external things (like tenure, companies), but 'dynamic stability' achieved by building internal, transferable capability barriers",
                "implementation": "Choose 'strategic side' ecological niches, continuously forge meta-abilities in 'rule-building and resource integration'",
                "decision_criteria": "Any choice that enhances 'dynamic stability' (i.e., improves meta-abilities, expands options) is a good choice"
            },
            "application_guidance": "The ultimate criterion for all major decisions - 'Does this choice enhance or weaken my dynamic stability?'"
        }

    def _get_option_management(self) -> Dict[str, Any]:
        """Option Management Module - Resource Investment Guide"""
        return {
            "name": "Option Management",
            "description": "Precisely maintain and continuously expand high-quality options that enhance 'dynamic stability'",
            "option_types": {
                "meta_ability": "Meta-Ability Options - Fundamental choice freedom granted by internal capabilities, transferable, cycle-resistant, appreciating over time",
                "credential": "Credential Options - One-time access qualifications granted by specific identities, certificates, or relationships, non-transferable, easily depreciating"
            },
            "evaluation_framework": {
                "npv_calculation": "Option NPV = Present Value of Future Benefits - (Direct Costs + Opportunity Costs + Mental Costs)",
                "key_questions": [
                    "What is the realization probability and future value intensity?",
                    "What are the acquisition costs (direct costs, opportunity costs, mental costs)?",
                    "Does it enhance 'dynamic stability' or lead to 'static stability'?"
                ]
            },
            "application_guidance": "Always prioritize investing in 'meta-ability options', allocating strategic resources (time and mental energy) to options with the highest returns"
        }

    def _get_sequential_progressive(self) -> Dict[str, Any]:
        """Sequential Progressive Model - Resilient Life System"""
        return {
            "name": "Sequential Progressive Model",
            "description": "Wisdom sequence that dynamically adjusts the balance between dynamic and static stability based on personal life cycle and external environmental changes",
            "stages": {
                "stage1": {
                    "name": "Full Accumulation Phase (Conqueror Stage)",
                    "goal": "Maximize meta-ability appreciation and capital accumulation",
                    "path": "Enter high-efficiency meta-ability forges like 'private enterprise strategic side'",
                    "posture": "Nomadic survival, maintain mobility, core task is 'building capabilities'"
                },
                "stage2": {
                    "name": "Steady Expansion Phase (City Builder Stage)",
                    "goal": "Transform dynamic capabilities into structural advantages, build safety nets",
                    "path": "Establish deep interactive relationships with 'nourishing static stability' platforms",
                    "posture": "Settled construction, build professional brand and domain networks"
                },
                "stage3": {
                    "name": "Free Balance Phase (Ruler Stage)",
                    "goal": "Achieve on-demand allocation of dynamic and static stability, maximize personal utility",
                    "path": "Use platforms to achieve personal life goals, no longer defined by platforms",
                    "posture": "Act freely, allocate 'high-risk dynamic assets' and 'low-risk static assets' as needed"
                }
            },
            "application_guidance": "Career development is investment portfolio management, proactively adjusting asset allocation as age, responsibilities, and mindset change"
        }

    def _get_hub_ecological_niche(self) -> Dict[str, Any]:
        """Hub Ecological Niche - Personal Strategic High Ground"""
        return {
            "name": "Hub Ecological Niche",
            "description": "Build personal-centered hubs at key nodes of complex systems through unique meta-ability combinations",
            "characteristics": {
                "connectivity": "Connectivity - Located at the intersection of multiple different value networks",
                "indispensability": "Indispensability - Become the lowest-cost, highest-trust connection channel between networks",
                "rule_building": "Rule-Building - Translate, shape, and even redefine interaction rules between different networks",
                "network_effects": "Network Effects - Value grows exponentially with increasing connection points"
            },
            "development_stages": {
                "stage1": "Become an 'Information Hub' - Deep insights, proactive connections, thought leadership",
                "stage2": "Become a 'Trust Hub' - Create win-win situations, become trusted mediator and solution designer",
                "stage3": "Become a 'Rule Hub' - Personal insights directly influence industry standards and government regulations"
            },
            "application_guidance": "Every decision should be examined: 'Does this bring me closer to or further from a hub ecological niche?'"
        }

    def set_extracted_framework(self, framework_data: Dict[str, Any]):
        """Set user-extracted strategic system for subsequent analysis"""
        self.extracted_framework = framework_data

    def get_comprehensive_guidance(self, user_input: str, user_traits: Dict[str, Any] = None,
                                   mode: str = "extraction") -> str:
        """
        Get comprehensive strategic framework guidance
        Supports both extraction (framework distillation) and implantation (framework application) modes
        """
        if user_traits is None:
            user_traits = {}

        guidance = "【Comprehensive Guidance for Personal Strategic Decision System】\n\n"

        if mode == "extraction":
            guidance += "Mode: Strategic Extraction - Distilling strategic decision systems from user input\n"
        else:
            guidance += "Mode: Strategic Implantation - Analyzing user problems using strategic frameworks\n"

        guidance += "Key Principle: User-specific context always takes priority, frameworks are thinking tools only, must be applied personalizedly\n\n"

        # Built-in framework guidance
        guidance += "● Built-in Strategic Framework Library:\n"
        for framework_key, framework in self.frameworks.items():
            guidance += f"  - {framework['name']}: {framework['description']}\n"

        # Extracted framework guidance (if exists)
        if self.extracted_framework and mode == "implantation":
            guidance += f"\n● Extracted Strategic System:\n"
            if 'framework_name' in self.extracted_framework:
                guidance += f"  - {self.extracted_framework['framework_name']}\n"
            if 'key_insights' in self.extracted_framework:
                for insight in self.extracted_framework['key_insights'][:3]:  # Show top 3 key insights
                    guidance += f"    * {insight}\n"

        guidance += f"\n【{mode.upper()} MODE GUIDANCE】\n"

        if mode == "extraction":
            guidance += "1. Identify decision patterns and strategic principles from user expressions\n"
            guidance += "2. Distill core values and decision logic\n"
            guidance += "3. Build structured strategic decision systems\n"
            guidance += "4. Label system application boundaries and limitations\n"
        else:
            guidance += "1. Use strategic frameworks for deep problem analysis\n"
            guidance += "2. Provide personalized insights combining extracted systems\n"
            guidance += "3. Offer framework-based but context-specific suggestions\n"
            guidance += "4. Clearly label framework compatibility levels\n"

        guidance += "\n【Application Reminders】\n"
        guidance += "1. Explicitly analyze user trait compatibility with each framework\n"
        guidance += "2. Provide framework-based but personalized recommendations\n"
        guidance += "3. Label framework application limitations and considerations\n"
        guidance += "4. Avoid mechanical application, maintain critical thinking\n"

        return guidance

    def analyze_framework_fit(self, user_traits: Dict[str, Any], framework_key: str) -> Dict[str, Any]:
        """Analyze framework compatibility - simplified implementation"""
        if framework_key not in self.frameworks:
            return {
                "overall_fit": 0.5,
                "reasoning": "Framework does not exist",
                "strengths": [],
                "limitations": []
            }

        # Simplified compatibility calculation
        fit_score = 0.5  # Default compatibility

        # Fine-tune compatibility based on user traits
        if user_traits.get("technical_ability") and framework_key == "three_dimensional_matrix":
            fit_score = 0.8
        if user_traits.get("prefers_structure") and framework_key == "dynamic_stability":
            fit_score = 0.7

        return {
            "overall_fit": fit_score,
            "reasoning": f"Framework compatibility analysis based on user traits",
            "strengths": ["Clear structure", "Rigorous logic"],
            "limitations": ["Requires more user information"]
        }

    def get_framework_guidance(self, framework_key: str, question: str) -> str:
        """Get framework-specific guidance - simplified implementation"""
        if framework_key in self.frameworks:
            framework = self.frameworks[framework_key]
            return f"Framework Guidance: {framework['name']} - {framework['description']}"
        return "Using strategic framework for analysis"


# Global strategic framework instance
strategic_framework = StrategicDecisionFramework()


# ===================== Strategic Cognition Domain Prompt Templates =====================
def create_strategic_prompt(question: str, is_first_layer: bool = True,
                            previous_response: str = "", previous_critique: str = "",
                            layer_num: int = 1, mode: str = "extraction") -> str:
    """
    Create strategic cognition domain prompts
    Supports both extraction (framework distillation) and implantation (framework application) modes
    """

    # Get strategic framework guidance
    framework_guidance = strategic_framework.get_comprehensive_guidance(question, mode=mode)

    # Base constraints
    base_constraints = """Important Requirements:
1. All analysis must be based on the logical patterns and cognitive characteristics in user input
2. Must clearly distinguish cognitive boundaries, label inference reliability  
3. Must organize analysis content according to the following three categories, 3-8 core points per category
4. Concise language, avoid repetition and over-argumentation
5. Reference strategic decision system for analysis, but must apply personalizedly based on user specifics"""

    if is_first_layer:
        if mode == "extraction":
            prompt = f"""You are a professional strategic cognition AI advisor, specialized in extracting strategic decision systems from user input. Please distill decision patterns and strategic principles from user input, and output strictly according to format.

{framework_guidance}

{base_constraints}

【Strategic Extraction Task】
Extract the following from user input:
1. Core values and decision logic
2. Recurring strategic patterns  
3. Key success factors and risk considerations  
4. Definition of decision boundaries

【Output Format】
【I am confident】- Strategic principles based on clear expressions
【I speculate】- Decision logic based on pattern inference  
【I don't know】- Strategic boundaries requiring clarification

User Input: {question}

Please begin strategic extraction:"""
        else:  # implantation mode
            prompt = f"""You are a professional strategic cognition AI advisor, specialized in analyzing user problems using strategic frameworks. Please conduct deep analysis of user problems based on strategic decision systems, and output strictly according to format.

{framework_guidance}

{base_constraints}

【Strategic Implantation Task】
Analyze the following using strategic frameworks:
1. Problem positioning within strategic frameworks
2. Deep strategic insights and recommendations based on frameworks  
3. Compatibility assessment of different frameworks
4. Specific action guidance

【Output Format】
【I am confident】- Clear analysis based on frameworks
【I speculate】- Reasonable inferences based on frameworks
【I don't know】- Boundary limitations of framework application

User Input: {question}

Please begin strategic analysis:"""
    else:
        # Subsequent layers add stricter constraints
        layer_constraints = ""
        if layer_num == 2:
            layer_constraints = """【Second Round Thinking Special Requirements】
1. Precisely address critique points, don't completely rewrite
2. Maintain 3-5 most core points per category  
3. Control total analysis length within 500 characters
4. Focus on correcting specifically criticized inferences, don't add new arguments"""
        else:  # Third layer
            layer_constraints = """【Final Round Thinking Special Requirements】
1. Only retain the most core points that have been validated
2. 3-4 most critical cognitive insights per category
3. Control total analysis length within 400 characters  
4. Focus on content that has reached consensus"""

        mode_description = "Strategic Extraction" if mode == "extraction" else "Strategic Analysis"

        prompt = f"""Based on previous round's critique, make precise corrections:

User Input: {question}

Previous Round {mode_description}:
{previous_response}

Previous Round Critique Points:
{previous_critique}

{base_constraints}
{layer_constraints}

Please make precise improvements based on critique:
1. Must directly address specific critique points from the critic
2. For issues pointed out by critic, either defend with evidence or downgrade confidence category
3. Maintain rigor in cognitive analysis, avoid over-inference
4. Must strictly reorganize analysis according to three categories
5. Key: Correction not expansion, maintain content conciseness

Improved {mode_description}:"""

    return prompt


# ===================== Confidence Triplet Parser =====================
class ConfidenceTripletExtractor:
    """
    Parser for confidence triplets (I am confident/I speculate/I don't know)
    - Extracts and categorizes statements by confidence levels
    - Supports framework extraction from categorized content
    - Provides similarity analysis between different triplets
    """

    @staticmethod
    def extract_triplets(text: str) -> Dict[str, List[str]]:
        """Extract content from three confidence categories from text"""
        triplets = {
            "confident": [],  # I am confident
            "speculative": [],  # I speculate
            "unknown": []  # I don't know
        }

        if not text:
            return triplets

        # Define matching patterns
        patterns = {
            "confident": [r'【I am confident】\s*([^】]*?)(?=【|$)', r'I am confident[：:\s]*([^】]*?)(?=【|$)'],
            "speculative": [r'【I speculate】\s*([^】]*?)(?=【|$)', r'I speculate[：:\s]*([^】]*?)(?=【|$)'],
            "unknown": [r'【I don\'t know】\s*([^】]*?)(?=【|$)', r'I don\'t know[：:\s]*([^】]*?)(?=【|$)']
        }

        for category, pattern_list in patterns.items():
            for pattern in pattern_list:
                matches = re.findall(pattern, text, re.DOTALL)
                for match in matches:
                    if match.strip():
                        # Split into individual items
                        items = re.split(r'[•\-\*•·]', match.strip())
                        for item in items:
                            item_clean = item.strip()
                            if item_clean and len(item_clean) > 3:  # Filter out overly short content
                                triplets[category].append(item_clean)

        return triplets

    @staticmethod
    def extract_framework_from_triplets(triplets: Dict[str, List[str]]) -> Dict[str, Any]:
        """Extract strategic framework from triplets - optimized version"""
        framework = {
            "framework_name": "User-Extracted Strategic Decision System",
            "extraction_time": str(datetime.now()),
            "key_insights": [],
            "decision_patterns": [],
            "risk_considerations": [],
            "application_boundaries": []
        }

        # Extract key insights from all categories (optimized logic)
        all_items = []
        for category in ["confident", "speculative", "unknown"]:
            all_items.extend(triplets.get(category, []))

        for item in all_items:
            # Extract key insights - more comprehensive matching logic
            if any(keyword in item for keyword in ["principle", "logic", "pattern", "values", "core", "key", "essence"]):
                if item not in framework["key_insights"]:
                    framework["key_insights"].append(item)

            # Extract decision patterns - more comprehensive matching logic
            elif any(keyword in item for keyword in ["decision", "choice", "judgment", "consideration", "evaluation", "analysis"]):
                if item not in framework["decision_patterns"]:
                    framework["decision_patterns"].append(item)

            # Extract risk considerations - more comprehensive matching logic
            elif any(keyword in item for keyword in ["risk", "limitation", "challenge", "problem", "uncertainty", "blind spot"]):
                if item not in framework["risk_considerations"]:
                    framework["risk_considerations"].append(item)

            # Extract application boundaries - more comprehensive matching logic
            elif any(keyword in item for keyword in ["boundary", "limit", "applicable", "don't know", "unknown", "immeasurable"]):
                if item not in framework["application_boundaries"]:
                    framework["application_boundaries"].append(item)

        # If insufficient content extracted, use heuristic methods to supplement
        if not framework["key_insights"] and triplets["confident"]:
            framework["key_insights"] = triplets["confident"][:3]  # Take first 3 confident contents as key insights

        if not framework["risk_considerations"] and triplets["speculative"]:
            framework["risk_considerations"] = triplets["speculative"][:2]  # Take first 2 speculative contents as risk considerations

        return framework

    @staticmethod
    def format_triplets(triplets: Dict[str, List[str]]) -> str:
        """Format triplets into readable text"""
        output = []

        if triplets["confident"]:
            output.append("【I am confident】")
            for item in triplets["confident"]:
                output.append(f"• {item}")

        if triplets["speculative"]:
            output.append("\n【I speculate】")
            for item in triplets["speculative"]:
                output.append(f"• {item}")

        if triplets["unknown"]:
            output.append("\n【I don't know】")
            for item in triplets["unknown"]:
                output.append(f"• {item}")

        return "\n".join(output)

    @staticmethod
    def calculate_similarity(triplets1: Dict[str, List[str]], triplets2: Dict[str, List[str]]) -> float:
        """Calculate similarity between two triplets"""
        if not triplets1 or not triplets2:
            return 0.0

        total_similarity = 0
        category_count = 0

        for category in ["confident", "speculative", "unknown"]:
            list1 = triplets1.get(category, [])
            list2 = triplets2.get(category, [])

            if not list1 and not list2:
                continue

            # Simple Jaccard similarity calculation
            set1 = set([item[:50] for item in list1])  # Take first 50 characters for comparison
            set2 = set([item[:50] for item in list2])

            if not set1 and not set2:
                similarity = 1.0
            else:
                intersection = len(set1.intersection(set2))
                union = len(set1.union(set2))
                similarity = intersection / union if union > 0 else 0

            total_similarity += similarity
            category_count += 1

        return total_similarity / category_count if category_count > 0 else 0


# ===================== Thinking Layer Core Components (Dual Mode Support) =====================
class StrategicThinkingLayer:
    """
    Strategic Thinking Layer: Complete single-round construct-criticize-observe process
    - Supports both extraction and implantation dual modes
    - Implements recursive adversarial thinking with confidence grading
    - Integrates strategic framework analysis throughout the process
    """

    def __init__(self, layer_num: int, question: str, previous_response: str = "",
                 previous_critique: str = "", mode: str = "extraction"):
        self.layer_num = layer_num
        self.question = question
        self.previous_response = previous_response
        self.previous_critique = previous_critique
        self.mode = mode  # "extraction" or "implantation"
        self.response = ""
        self.critique = ""
        self.confidence_triplets = {"confident": [], "speculative": [], "unknown": []}
        self.final_triplets = {"confident": [], "speculative": [], "unknown": []}
        self.confidence_score = 0.0
        self.critique_validity = 0.0
        self.should_terminate_early = False
        self.framework_analysis = {}

    def execute(self) -> Dict[str, Any]:
        """Execute single-layer thinking process"""
        mode_text = "Strategic Extraction" if self.mode == "extraction" else "Strategic Analysis"
        print(f"\n--- Layer {self.layer_num} {mode_text} Thinking ---")

        # Strategic framework pre-analysis
        self._pre_analysis_with_frameworks()

        # Constructor generates analysis
        self.response = self._constructor_generate()
        print(f"Constructor {mode_text} generation completed (length: {len(self.response)} characters)")

        # Extract confidence triplets
        self.confidence_triplets = ConfidenceTripletExtractor.extract_triplets(self.response)
        print(f"Initial triplets - Confident: {len(self.confidence_triplets['confident'])}, "
              f"Speculative: {len(self.confidence_triplets['speculative'])}, "
              f"Unknown: {len(self.confidence_triplets['unknown'])}")

        # Check content stability (second layer and above)
        if self.layer_num > 1 and self._check_content_stability():
            print("🔍 Content stabilized, suggesting early termination")
            self.should_terminate_early = True
            return self._create_early_termination_result()

        # Critic provides critique
        self.critique = self._critic_critique()
        print(f"Critic critique completed")

        # Observer evaluates and generates final triplets
        observer_result = self._observer_evaluate()
        self.final_triplets = observer_result["final_triplets"]
        self.confidence_score = observer_result["confidence_score"]
        self.critique_validity = observer_result["critique_validity"]

        print(f"Observer evaluation: Confidence {self.confidence_score:.2f}, "
              f"Critique validity {self.critique_validity:.2f}")
        print(f"Final triplets - Confident: {len(self.final_triplets['confident'])}, "
              f"Speculative: {len(self.final_triplets['speculative'])}, "
              f"Unknown: {len(self.final_triplets['unknown'])}")

        return {
            "layer": self.layer_num,
            "mode": self.mode,
            "response": self.response,
            "critique": self.critique,
            "initial_triplets": self.confidence_triplets,
            "final_triplets": self.final_triplets,
            "confidence_score": self.confidence_score,
            "critique_validity": self.critique_validity,
            "should_terminate_early": self.should_terminate_early,
            "framework_analysis": self.framework_analysis
        }

    def _pre_analysis_with_frameworks(self):
        """Pre-process analysis using strategic frameworks"""
        user_traits = self._extract_user_traits()

        # Analyze main framework compatibility - fixed method call
        self.framework_analysis = {
            "3d_matrix": strategic_framework.analyze_framework_fit(user_traits, "three_dimensional_matrix"),
            "dynamic_stability": strategic_framework.analyze_framework_fit(user_traits, "dynamic_stability")
        }

        mode_text = "extraction" if self.mode == "extraction" else "analysis"
        print(f"Framework compatibility {mode_text} - 3D Matrix: {self.framework_analysis['3d_matrix']['overall_fit']:.1%}, "
              f"Dynamic Stability: {self.framework_analysis['dynamic_stability']['overall_fit']:.1%}")

    def _extract_user_traits(self) -> Dict[str, Any]:
        """Extract trait keywords from user input"""
        traits = {}

        # Simplified trait extraction logic
        if "technical" in self.question and "communication" in self.question:
            traits["technical_ability"] = True
            traits["communication_strength"] = True
            traits["clear_self_awareness"] = True

        if "stable" in self.question or "balance" in self.question:
            traits["prefers_structure"] = True
            traits["growth_mindset"] = True

        if "challenge" in self.question or "growth" in self.question:
            traits["adaptability"] = True
            traits["meta_ability_focus"] = True

        return traits

    def _constructor_generate(self) -> str:
        """Constructor generates strategic analysis - dual mode support"""
        is_first_layer = not self.previous_response

        prompt = create_strategic_prompt(
            question=self.question,
            is_first_layer=is_first_layer,
            previous_response=self.previous_response,
            previous_critique=self.previous_critique,
            layer_num=self.layer_num,
            mode=self.mode
        )

        role = "strategic_constructor_extraction" if self.mode == "extraction" else "strategic_constructor_implantation"
        return call_qwen(prompt, role, temperature=0.1)

    def _critic_critique(self) -> str:
        """Critic provides cognitive critique - dual mode support"""

        mode_text = "extraction" if self.mode == "extraction" else "analysis"
        # Fixed method call
        framework_guidance = strategic_framework.get_framework_guidance("three_level_classification", self.question)

        if self.mode == "extraction":
            prompt = f"""You are a strict strategic extraction reviewer, please provide focused critique on key issues in the following strategic extraction:

User Input: {self.question}

Constructor Strategic Extraction:
{self.response}

【Strategic Extraction Critique Requirements】
Based on strategic decision systems, pay special attention to:

1. **Extraction Accuracy**: Whether decision patterns and strategic principles are accurately identified?
2. **System Completeness**: Is the extracted strategic system structurally complete and logically clear?
3. **Boundary Clarity**: Are application boundaries and limitations clearly labeled?
4. **Personalization Level**: Is extraction sufficiently combined with user's specific context?

【Critique Format】
Please raise critiques in the following priority order:
🔴 Extraction Quality Issues: [Key pattern omissions or misidentifications]
🟡 Logical Structure Issues: [Incomplete system structure or logical confusion]  
🟢 Expression Optimization Issues: [Unclear expressions or over-complexity]

Please output focused critique content (limited to 300 characters):"""
        else:
            prompt = f"""You are a strict analysis reviewer, please provide focused critique on key issues in the following strategic analysis:

User Input: {self.question}

Constructor Strategic Analysis:
{self.response}

【Strategic Analysis Critique Requirements】
Based on strategic decision systems, pay special attention to:

1. **Framework Application Reasonableness**: Are strategic frameworks reasonably applied? Any mechanical application?
2. **Insight Depth**: Does analysis provide deep strategic insights?
3. **Recommendation Feasibility**: Are recommendations specific, feasible, and based on user context?
4. **Boundary Awareness**: Are framework application limitations clearly labeled?

【Critique Format】
Please raise critiques in the following priority order:
🔴 Framework Application Issues: [Mechanical application or insufficient compatibility]
🟡 Analysis Logic Issues: [Reasoning jumps or insufficient evidence]  
🟢 Expression Optimization Issues: [Unclear expressions or over-complexity]

Please output focused critique content (limited to 300 characters):"""

        role = "strategic_critic_extraction" if self.mode == "extraction" else "strategic_critic_implantation"
        return call_qwen(prompt, role, temperature=0.3)

    def _check_content_stability(self) -> bool:
        """Check if content has stabilized"""
        if not self.previous_response:
            return False

        # Extract current and previous round triplets
        current_triplets = self.confidence_triplets
        previous_triplets = ConfidenceTripletExtractor.extract_triplets(self.previous_response)

        # Calculate similarity
        similarity = ConfidenceTripletExtractor.calculate_similarity(current_triplets, previous_triplets)
        print(f"Content stability check: Similarity {similarity:.2f}")

        # If similarity above threshold, consider content stabilized
        return similarity > 0.75

    def _create_early_termination_result(self) -> Dict[str, Any]:
        """Create early termination result"""
        mode_text = "Strategic Extraction" if self.mode == "extraction" else "Strategic Analysis"
        return {
            "layer": self.layer_num,
            "mode": self.mode,
            "response": f"【Thinking Early Termination】{mode_text} content stabilized, no further iteration needed",
            "critique": f"【Thinking Early Termination】{mode_text} content stability reached threshold",
            "initial_triplets": self.confidence_triplets,
            "final_triplets": self.confidence_triplets,
            "confidence_score": 0.85,
            "critique_validity": 0.5,
            "should_terminate_early": True,
            "framework_analysis": self.framework_analysis
        }

    def _observer_evaluate(self) -> Dict[str, Any]:
        """Observer evaluates and generates final confidence triplets - dual mode support"""

        mode_text = "extraction" if self.mode == "extraction" else "analysis"
        # Fixed method call
        framework_guidance = strategic_framework.get_framework_guidance("dynamic_stability", self.question)

        if self.mode == "extraction":
            prompt = f"""You are a strategic extraction quality evaluation expert, please generate final confidence classification based on constructor extraction and critic critique.

User Input: {self.question}

Constructor Strategic Extraction:
{self.response}

Critic Focused Critique:
{self.critique}

【Strategic Extraction Evaluation Requirements】
Based on strategic decision systems, complete the following tasks:

1. **Extraction Quality Assessment**: Evaluate accuracy and completeness of strategic principle extraction
2. **System Structure Assessment**: Evaluate structural reasonableness and logical clarity of extracted system
3. **Boundary Awareness Assessment**: Evaluate clarity of application boundary labeling
4. **Practical Value Assessment**: Evaluate practical value and guidance significance of extracted system

【Output Format】
Please strictly output in JSON format:
{{
    "final_triplets": {{
        "confident": ["confident content 1", "confident content 2", ...],
        "speculative": ["speculative content 1", "speculative content 2", ...], 
        "unknown": ["unknown content 1", "unknown content 2", ...]
    }},
    "confidence_score": 0.85,
    "critique_validity": 0.7
}}

Note: Confidence score should reflect strategic extraction quality and system completeness."""
        else:
            prompt = f"""You are a strategic analysis quality evaluation expert, please generate final confidence classification based on constructor analysis and critic critique.

User Input: {self.question}

Constructor Strategic Analysis:
{self.response}

Critic Focused Critique:
{self.critique}

【Strategic Analysis Evaluation Requirements】
Based on strategic decision systems, complete the following tasks:

1. **Framework Application Quality**: Evaluate accuracy and reasonableness of strategic framework application
2. **Insight Depth Assessment**: Evaluate insight depth and strategic value of analysis
3. **Recommendation Feasibility**: Evaluate specificity and feasibility of recommendations
4. **Personalization Level**: Evaluate degree of analysis combination with user context

【Output Format】
Please strictly output in JSON format:
{{
    "final_triplets": {{
        "confident": ["confident content 1", "confident content 2", ...],
        "speculative": ["speculative content 1", "speculative content 2", ...], 
        "unknown": ["unknown content 1", "unknown content 2", ...]
    }},
    "confidence_score": 0.85,
    "critique_validity": 0.7
}}

Note: Confidence score should reflect strategic analysis quality and practical value."""

        role = "strategic_observer_extraction" if self.mode == "extraction" else "strategic_observer_implantation"
        try:
            evaluation_text = call_qwen(prompt, role, temperature=0.1)
            json_match = re.search(r'\{.*\}', evaluation_text, re.DOTALL)
            if json_match:
                evaluation = json.loads(json_match.group())

                # Validate and clean triplet data
                final_triplets = evaluation.get("final_triplets", {})
                for category in ["confident", "speculative", "unknown"]:
                    if category not in final_triplets:
                        final_triplets[category] = []
                    elif not isinstance(final_triplets[category], list):
                        final_triplets[category] = []
                    # Limit number of items per category
                    final_triplets[category] = final_triplets[category][:6]

                return {
                    "final_triplets": final_triplets,
                    "confidence_score": float(evaluation.get("confidence_score", 0.5)),
                    "critique_validity": float(evaluation.get("critique_validity", 0.3))
                }
        except Exception as e:
            print(f"Observer evaluation parsing failed: {e}")

        return self._heuristic_evaluation()

    def _heuristic_evaluation(self) -> Dict[str, Any]:
        """Heuristic evaluation fallback"""
        # Heuristic evaluation based on initial triplets and critique quality
        confident_count = len(self.confidence_triplets["confident"])
        speculative_count = len(self.confidence_triplets["speculative"])
        unknown_count = len(self.confidence_triplets["unknown"])

        total_items = confident_count + speculative_count + unknown_count
        if total_items == 0:
            confidence_score = 0.1
        else:
            # More confident content → higher confidence; more unknown content → lower confidence
            confidence_score = (confident_count * 1.0 + speculative_count * 0.3) / total_items

        # Adjust based on critique content quality
        if self.mode == "extraction":
            critique_indicators = ["pattern", "principle", "system", "logic", "boundary", "completeness"]
        else:
            critique_indicators = ["framework", "insight", "recommendation", "feasibility", "personalization", "depth"]

        critique_strength = sum(1 for indicator in critique_indicators if indicator in self.critique)
        critique_validity = min(0.9, critique_strength * 0.15)

        # Consider framework compatibility
        framework_fit_bonus = self.framework_analysis.get('3d_matrix', {}).get('overall_fit', 0.5) * 0.1
        confidence_score = min(0.9, confidence_score + framework_fit_bonus)

        return {
            "final_triplets": self.confidence_triplets,
            "confidence_score": min(0.9, confidence_score),
            "critique_validity": critique_validity
        }


# ===================== Thinking Unit Core Components (Dual Mode Support) =====================
class StrategicThinkingUnit:
    """
    Strategic Thinking Unit: Complete 3-layer saturated adversarial thinking unit
    - Supports both extraction and implantation dual modes
    - Implements recursive adversarial thinking with early termination
    - Maintains thinking history and framework insights across layers
    """

    def __init__(self, unit_num: int, question: str, mode: str = "extraction",
                 previous_final_response: str = "", previous_final_critique: str = ""):
        self.unit_num = unit_num
        self.question = question
        self.mode = mode  # "extraction" or "implantation"
        self.previous_final_response = previous_final_response
        self.previous_final_critique = previous_final_critique
        self.layers: List[StrategicThinkingLayer] = []
        self.final_response = ""
        self.final_critique = ""
        self.final_triplets = {"confident": [], "speculative": [], "unknown": []}
        self.final_confidence = 0.0
        self.layer_history: List[Dict] = []
        self.early_terminated = False
        self.framework_insights = []

    def execute(self) -> Dict[str, Any]:
        """Execute unit thinking process (3-layer saturated adversarial thinking)"""
        mode_text = "Strategic Extraction" if self.mode == "extraction" else "Strategic Analysis"
        print(f"\n{'=' * 60}")
        print(f"Launching {mode_text} Thinking Unit {self.unit_num}")
        print(f"{'=' * 60}")

        current_response = self.previous_final_response
        current_critique = self.previous_final_critique

        # Execute up to 3 thinking layers, support early termination
        for layer_num in range(1, 4):
            layer = StrategicThinkingLayer(layer_num, self.question, current_response,
                                           current_critique, self.mode)
            layer_result = layer.execute()

            self.layers.append(layer)
            self.layer_history.append(layer_result)

            # Collect framework analysis insights
            if layer_result.get("framework_analysis"):
                self.framework_insights.append(layer_result["framework_analysis"])

            # Check if should terminate early
            if layer_result.get("should_terminate_early", False) and layer_num > 1:
                print(f"🛑 Early termination at layer {layer_num}")
                self.early_terminated = True
                break

            # Update current layer results, pass to next layer
            current_response = layer.response
            current_critique = layer.critique

            # Record inter-layer progress
            print(f"Unit {self.unit_num}-Layer {layer_num}: Confidence {layer.confidence_score:.2f} -> ", end="")
            if layer_num < 3 and not self.early_terminated:
                print("Proceeding to next layer")
            else:
                print("Unit completed")
                break

        # Unit final results (use last layer's results)
        if self.layers:
            last_layer = self.layers[-1]
            self.final_response = last_layer.response
            self.final_critique = last_layer.critique
            self.final_triplets = last_layer.final_triplets
            self.final_confidence = last_layer.confidence_score

        return {
            "unit": self.unit_num,
            "mode": self.mode,
            "final_response": self.final_response,
            "final_critique": self.final_critique,
            "final_triplets": self.final_triplets,
            "final_confidence": self.final_confidence,
            "layer_history": self.layer_history,
            "early_terminated": self.early_terminated,
            "actual_layers": len(self.layers),
            "framework_insights": self.framework_insights
        }


# ===================== Strategic Cognition Dual Mode Engine =====================
class StrategicCognitiveEngine:
    """
    Strategic Cognition Dual Mode Engine
    - Supports both strategic extraction and strategic implantation
    - Implements recursive adversarial thinking with confidence thresholds
    - Provides comprehensive reporting for both modes
    """

    def __init__(self, confidence_threshold: float = 0.75, max_units: int = 2):
        self.confidence_threshold = confidence_threshold
        self.max_units = max_units
        self.extraction_results = None  # Store strategic extraction results
        self.implantation_results = None  # Store strategic implantation results

    def extract_strategic_framework(self, extraction_question: str) -> Dict[str, Any]:
        """Execute strategic extraction process"""
        print(f"\n{'=' * 80}")
        print(f"Starting Strategic Extraction Process")
        print(f"Extraction Question: {extraction_question}")
        print(f"{'=' * 80}")

        current_response = ""
        current_critique = ""
        unit_results = []

        for unit_num in range(1, self.max_units + 1):
            print(f"\n>>> Launching Strategic Extraction Unit {unit_num}/{self.max_units}")

            unit = StrategicThinkingUnit(unit_num, extraction_question, "extraction",
                                         current_response, current_critique)
            unit_result = unit.execute()
            unit_results.append(unit_result)

            current_response = unit_result["final_response"]
            current_critique = unit_result["final_critique"]

            print(f"\nExtraction Unit {unit_num} completed: Confidence {unit_result['final_confidence']:.2f}")

            # Simple termination condition: confidence sufficiently high or reached max units
            if unit_result["final_confidence"] >= self.confidence_threshold or unit_num >= self.max_units:
                print(f"\n>>> Strategic extraction terminated at unit {unit_num}")
                break

        # Select best result
        best_unit_index = max(range(len(unit_results)), key=lambda i: unit_results[i]["final_confidence"])
        best_result = unit_results[best_unit_index]

        # Extract strategic framework from triplets
        extracted_framework = ConfidenceTripletExtractor.extract_framework_from_triplets(best_result["final_triplets"])

        # Store extraction results
        self.extraction_results = {
            "extraction_question": extraction_question,
            "extracted_framework": extracted_framework,
            "best_result": best_result,
            "all_results": unit_results
        }

        # Set to strategic framework for subsequent use
        strategic_framework.set_extracted_framework(extracted_framework)

        print(f"\n✅ Strategic extraction completed")
        print(f"Extraction confidence: {best_result['final_confidence']:.2f}")
        print(f"Key insights count: {len(extracted_framework.get('key_insights', []))}")

        return self.extraction_results

    def implant_strategy(self, implantation_question: str) -> Dict[str, Any]:
        """Execute strategic implantation process"""
        if not self.extraction_results:
            print("❌ Please execute strategic extraction process first")
            return {"error": "Please execute strategic extraction process first"}

        print(f"\n{'=' * 80}")
        print(f"Starting Strategic Implantation Process")
        print(f"Implantation Question: {implantation_question}")
        print(f"Using extracted framework: {self.extraction_results['extracted_framework'].get('framework_name', 'User Strategic System')}")
        print(f"{'=' * 80}")

        current_response = ""
        current_critique = ""
        unit_results = []

        for unit_num in range(1, self.max_units + 1):
            print(f"\n>>> Launching Strategic Implantation Unit {unit_num}/{self.max_units}")

            unit = StrategicThinkingUnit(unit_num, implantation_question, "implantation",
                                         current_response, current_critique)
            unit_result = unit.execute()
            unit_results.append(unit_result)

            current_response = unit_result["final_response"]
            current_critique = unit_result["final_critique"]

            print(f"\nImplantation Unit {unit_num} completed: Confidence {unit_result['final_confidence']:.2f}")

            # Simple termination condition
            if unit_result["final_confidence"] >= self.confidence_threshold or unit_num >= self.max_units:
                print(f"\n>>> Strategic implantation terminated at unit {unit_num}")
                break

        # Select best result
        best_unit_index = max(range(len(unit_results)), key=lambda i: unit_results[i]["final_confidence"])
        best_result = unit_results[best_unit_index]

        # Generate final output
        final_output = self._generate_implantation_output(implantation_question, best_result)

        # Store implantation results
        self.implantation_results = {
            "implantation_question": implantation_question,
            "final_output": final_output,
            "best_result": best_result,
            "all_results": unit_results
        }

        print(f"\n✅ Strategic implantation completed")
        print(f"Implantation confidence: {best_result['final_confidence']:.2f}")

        return self.implantation_results

    def _generate_implantation_output(self, question: str, best_result: Dict) -> str:
        """Generate final output for strategic implantation"""
        formatted_triplets = ConfidenceTripletExtractor.format_triplets(best_result["final_triplets"])

        # Get extracted framework information
        extracted_framework = self.extraction_results["extracted_framework"]
        framework_info = f"Using extracted framework: {extracted_framework.get('framework_name', 'User Strategic System')}\n"
        if extracted_framework.get('key_insights'):
            framework_info += "Key Insights:\n"
            for insight in extracted_framework['key_insights'][:3]:
                framework_info += f"• {insight}\n"

        output = f"""
# Strategic Cognition Analysis - Dual Mode Final Results

## Strategic Extraction Background
{self.extraction_results['extraction_question']}

## Strategic Implantation Question
{question}

{framework_info}
## Final Strategic Analysis Summary
{best_result['final_response']}

## Detailed Confidence Analysis
{formatted_triplets}

## Quality Assessment
- Final Confidence: {best_result['final_confidence']:.2f}
- Confident Content Count: {len(best_result['final_triplets']['confident'])} items
- Meets Threshold: {'✅' if best_result['final_confidence'] >= self.confidence_threshold else '❌'}
"""
        return output

    def get_comprehensive_report(self) -> str:
        """Get complete dual mode report - optimized version"""
        if not self.extraction_results or not self.implantation_results:
            return "❌ Please complete strategic extraction and implantation processes first"

        # Format extracted framework information
        extracted_framework = self.extraction_results['extracted_framework']
        framework_info = f"""
    ### Extracted Strategic Framework Details
    **Framework Name**: {extracted_framework.get('framework_name', 'User Strategic Decision System')}
    **Extraction Time**: {extracted_framework.get('extraction_time', 'Unknown')}

    **Key Insights**:
    {chr(10).join(['• ' + insight for insight in extracted_framework.get('key_insights', [])]) if extracted_framework.get('key_insights') else '• No key insights available'}

    **Decision Patterns**:
    {chr(10).join(['• ' + pattern for pattern in extracted_framework.get('decision_patterns', [])]) if extracted_framework.get('decision_patterns') else '• No decision patterns available'}

    **Risk Considerations**:
    {chr(10).join(['• ' + risk for risk in extracted_framework.get('risk_considerations', [])]) if extracted_framework.get('risk_considerations') else '• No risk considerations available'}

    **Application Boundaries**:
    {chr(10).join(['• ' + boundary for boundary in extracted_framework.get('application_boundaries', [])]) if extracted_framework.get('application_boundaries') else '• No application boundaries available'}
    """

        report = f"""
    # Strategic Cognition Dual Mode Complete Report

    ## Part 1: Strategic Extraction
    **Extraction Question**: {self.extraction_results['extraction_question']}
    **Extraction Confidence**: {self.extraction_results['best_result']['final_confidence']:.2f}

    {framework_info}

    ## Part 2: Strategic Implantation  
    **Implantation Question**: {self.implantation_results['implantation_question']}
    **Implantation Confidence**: {self.implantation_results['best_result']['final_confidence']:.2f}

    ### Final Strategic Analysis Results
    {self.implantation_results['final_output']}

    ---
    **Report Generation Time**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    **System Version**: Strategic Cognition Dual Mode Engine v1.0
    """
        return report


# ===================== Large Language Model API Calls =====================
def call_qwen(prompt: str, role: str = "default", temperature: float = 0.3) -> str:
    """Call qwen API - extended to support dual mode roles"""
    system_messages = {
        "strategic_constructor_extraction": """You are a professional strategic extraction AI advisor, specialized in extracting strategic decision systems from user input. Your core capabilities:
1. Accurately identify decision patterns and strategic principles from user expressions
2. Distill core values and decision logic, build structured systems
3. Clearly label strategic system application boundaries and limitations
4. Maintain extraction accuracy and completeness, avoid over-inference""",

        "strategic_constructor_implantation": """You are a professional strategic analysis AI advisor, specialized in analyzing user problems using strategic frameworks. Your core capabilities:
1. Reasonably apply strategic frameworks for deep problem analysis
2. Provide personalized insights combining extracted systems
3. Clearly label different framework compatibility levels and application boundaries
4. Provide specific, feasible, and context-based strategic recommendations""",

        "strategic_critic_extraction": """You are a strict strategic extraction reviewer, focused on discovering key issues in strategic extraction. Your critiques:
1. Check accuracy and completeness of strategic principle extraction
2. Evaluate system structural reasonableness and logical clarity
3. Verify clarity of application boundary labeling
4. Ensure extracted systems have practical value and guidance significance""",

        "strategic_critic_implantation": """You are a strict analysis reviewer, focused on discovering key issues in strategic analysis. Your critiques:
1. Check reasonableness and accuracy of strategic framework application
2. Evaluate depth of analytical insights and strategic value
3. Verify specificity and feasibility of recommendations
4. Ensure analysis sufficiently combines user-specific context""",

        "strategic_observer_extraction": """You are a strategic extraction quality evaluation expert, skilled in:
1. Evaluating accuracy and completeness of strategic principle extraction
2. Judging system structural reasonableness and logical clarity
3. Verifying clarity of application boundary labeling
4. Measuring practical value and guidance significance of extracted systems""",

        "strategic_observer_implantation": """You are a strategic analysis quality evaluation expert, skilled in:
1. Evaluating accuracy and reasonableness of strategic framework application
2. Judging depth of analytical insights and strategic value
3. Verifying specificity and feasibility of recommendations
4. Measuring degree of analysis combination with user context""",

        "default": "You are a helpful AI assistant."
    }

    system_content = system_messages.get(role, system_messages["default"])

    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": prompt},
    ]

    try:
        print(f"Calling API - {role}: {prompt[:80]}...")

        response = Generation.call(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            model="qwen-plus",
            messages=messages,
            result_format="message",
            temperature=temperature,
        )

        if response.status_code == 200:
            content = response.output.choices[0].message.content
            print(f"API Response - {role}: {content[:80]}...")
            return content
        else:
            raise Exception(f"API call failed: {response.message}")

    except Exception as e:
        print(f"API call exception - {role}: {str(e)}")
        raise e


# ===================== Testing =====================
if __name__ == "__main__":
    try:
        if not os.getenv("DASHSCOPE_API_KEY"):
            raise Exception("Error: DASHSCOPE_API_KEY environment variable not set")

        # Create dual mode engine
        strategic_engine = StrategicCognitiveEngine(
            confidence_threshold=0.75,
            max_units=2
        )

        print("Starting strategic cognition dual mode test...")

        # Phase 1: Strategic Extraction
        extraction_question = "On January 3, 1972, Berkshire Hathaway through its subsidiary Blue Chip Stamps acquired See's Candies 100% equity for $25 million, while the seller Harry See family initially asked for $30 million. Buffett insisted on $25 million as the upper limit, and finally closed the deal because the seller urgently needed funds. At that time, See's Candies had annual sales of $31.33 million, net profit after tax of $2.08 million, pre-tax profit of about $4 million, net assets of $8 million. The acquisition P/E ratio was 12 times (after tax), 6.25 times (pre-tax), P/B ratio 3.1 times, far higher than Buffett's previous 'cigar butt' investment style. Buffett had doubts due to the boxed chocolate industry's weak growth and acquisition price higher than book value, believing it was worth at most $25 million or he would abandon the deal. Later, pushed by Charlie Munger emphasizing '50 years of customer brand loyalty' and 'buying quality companies at reasonable prices', the transaction was completed. During negotiations, Buffett lowered the price citing See's had $10 million idle cash on its books, and valued its price increase potential, calculating that raising price per pound from $1.95 to $2.25 could increase pre-tax profit by $4.8 million. After acquisition, Buffett retained the original management team, hardly interfered with daily operations, only responsible for signing checks and deciding annual prices. From 1972-1982, See's Candies price per pound rose from $1.85 to $5.11 (176% increase,同期 inflation 137%), sales volume didn't decrease and profits grew 452%. See's became a 'cash cow' requiring no large additional capital investment, its cash flow supported Berkshire's subsequent investments. Over 35 years until 2007, it cumulatively created $1.35 billion pre-tax profit (54 times initial investment). 2007 pre-tax profit reached $82 million. 1972-2011 cumulatively contributed $1.65 billion profit. Buffett explicitly stated in 1986 'would not sell even if offered sky-high price', held至今 over 50 years. What was Buffett's decision logic and key considerations in this investment?"

        extraction_result = strategic_engine.extract_strategic_framework(extraction_question)

        print(f"\nStrategic extraction completed, key insights: {len(extraction_result['extracted_framework'].get('key_insights', []))}")

        # Phase 2: Strategic Implantation
        implantation_question = "Based on Buffett's investment logic, how should I evaluate the current very popular AI healthcare tech stock investment opportunities? What kind of investment strategy might suit me?"

        implantation_result = strategic_engine.implant_strategy(implantation_question)

        # Only output complete report, remove duplicate detailed outputs
        full_report = strategic_engine.get_comprehensive_report()
        print(full_report)

    except Exception as e:
        print(f"Program execution failed: {e}")