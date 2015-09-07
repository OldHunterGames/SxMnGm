import renpy.store as store
import renpy.exports as renpy

def set_table_status(status):
    table_status = status

def result_prercalculation(actor, partner):
    """
    preparing for score calculations on round end
    """
    if "passion" in actor.modifiers:
        actor.pleasure += actor.pleasure
    if "laceration" in actor.modifiers:
        actor.pain += actor.pain
    if "hysteria" in actor.modifiers:
        actor.shame += actor.shame
    if "tenderness" in actor.modifiers:
        partner.pleasure += partner.pleasure
    if "brutality" in actor.modifiers:
        partner.pain += partner.pain
    if "cruelty" in actor.modifiers:
        partner.shame += partner.shame

def calculated_result(actor, partner):
    """
    score calculation on round end
    """
    score = 0
    # using modifiers
    if "soft_maso" in actor.modifiers:
        if actor.pleasure > actor.pain:
            score += actor.pain
            actor.pain = 0
    if "black_maso" in actor.modifiers:
        score += actor.pain
        actor.pain = 0
    if "psi_maso" in actor.modifiers:
        score += actor.shame
        actor.shame = 0
    if "submission" in actor.modifiers:
        if actor.pleasure > actor.pain:
            score += actor.pain
            actor.pain = 0
        score += actor.shame
        actor.shame = 0
    if "enslavement" in actor.modifiers:
        score += actor.pain
        actor.pain = 0
        score += actor.shame
        actor.shame = 0
    if "sadism" in actor.modifiers:
        if "dominance" not in actor.modifiers:
            score += partner.pain
    if "mockery" in actor.modifiers:
        if "dominance" not in actor.modifiers:
            score += partner.shame
    if "dominance" in actor.modifiers:
        score += partner.shame
        score += partner.pain
    score += actor.pleasure - actor.pain - actor.shame
    return score