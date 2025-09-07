from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class State:
    menu_items: List[str] = field(default_factory=list)
    nutrition_data: Dict[str, Dict[str, float]] = field(default_factory=dict)
    recommendations: List[str] = field(default_factory=list)
    preferences: Dict[str, Any] = field(default_factory=dict)
    diversity_report: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "menu_items": self.menu_items,
            "nutrition_data": self.nutrition_data,
            "recommendations": self.recommendations,
            "preferences": self.preferences,
            "diversity_report": self.diversity_report,
        }
