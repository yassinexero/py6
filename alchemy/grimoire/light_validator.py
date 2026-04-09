def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = light_spell_allowed_ingredients()
    lowered: str = ingredients.lower()

    is_valid: bool = any(item in lowered for item in allowed)
    status: str = "VALID" if is_valid else "INVALID"

    return f"{ingredients} - {status}"
