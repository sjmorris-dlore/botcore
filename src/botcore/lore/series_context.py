"""
series_context.py
Series bible data for Guardian League and Thaumatropic Roots.

Shared by igbot (organic content generation) and any ad-generation or agent
that needs lore context. No channel-specific logic here — pure data plus
the build_series_context() composer.
"""

SERIES_OPTIONS = ["guardian_league", "thaumatropic_roots", "both"]

# ─── Book catalogs (for book-level LRU rotation within each series) ────────

SERIES_BOOKS = {
    "guardian_league": {
        1: "The Guardian of the Palace",
        2: "Stars in the Sand",
        3: "We're Going on an Elf Hunt",
        4: "The Song Unsung",
    },
    "thaumatropic_roots": {
        1: "Mother of Trees",
        2: "Bones of Cenaedth",
        3: "Secrets of Deara",
        4: "Shepherds of Truth",
    },
}

# Primary book number for each subject (aligns subject LRU with book LRU)
SUBJECT_PRIMARY_BOOK = {
    # Guardian League characters
    "Red": 1, "Galad": 1, "Grundle": 1, "Harry": 1,
    "Rocks": 2,
    "Scan": 3,
    # Guardian League world elements
    "The Palace": 1,
    "The Infected": 1,
    "Manhattan as a vertical city": 1,
    "The Guardian League organization": 1,
    "The interworld gateway": 2,
    "Talent abilities": 2,
    # Thaumatropic Roots characters
    "Elliah": 1, "Hughelas": 1, "Beldroth": 1, "Illiara": 1,
    "Trentius": 2,
    # Thaumatropic Roots world elements
    "The Mother of Trees": 1,
    "The magic system and Bereft": 1,
    "The five elven races": 1,
    "The Father of Stones and troll culture": 1,
    "The Breaking": 1,
    "Dragons — intelligent and telepathic": 2,
    "The Shield of Deara": 3,
}

# ─── Subject catalogs (pre-selection for LRU variety) ──────────────────────

CHARACTERS = {
    "guardian_league": ["Red", "Galad", "Grundle", "Harry", "Scan", "Rocks"],
    "thaumatropic_roots": ["Elliah", "Hughelas", "Beldroth", "Illiara", "Trentius"],
}

WORLD_ELEMENTS = {
    "guardian_league": [
        "The Palace",
        "The Infected",
        "Talent abilities",
        "The Guardian League organization",
        "The interworld gateway",
        "Manhattan as a vertical city",
    ],
    "thaumatropic_roots": [
        "The Mother of Trees",
        "The magic system and Bereft",
        "The five elven races",
        "The Father of Stones and troll culture",
        "Dragons — intelligent and telepathic",
        "The Shield of Deara",
        "The Breaking",
    ],
    "both": [
        "The connection between the two series",
        "How Thaumatropic Roots origins shaped Guardian League magic",
    ],
}

# Tropes — rotated for trope_post content type (instead of characters)
TROPES = [
    "monster-as-hero",
    "found family",
    "chosen without powers",
    "morally gray villain",
    "ancient being rediscovering purpose",
    "reluctant hero",
    "ordinary human in an extraordinary world",
    "the cost of loyalty",
    "power through connection not domination",
    "unlikely allies",
    "the weight of an ancient mistake",
    "humor as armor",
]

# ─── Series context (fed to AI — only relevant series included) ───────────

AUTHOR_BIO = """The author is Steven J. Morris (sjmorriswrites.com, Instagram: @steven.j.morris.writer).
He is an indie fantasy author who writes with warmth, humor, and heart. His prose is
character-driven, laced with wit even in dark moments, and grounded in emotional truth.
He writes for readers who love found family, underdogs, and fantasy that blends wonder with grit."""

# ─── Series context sub-sections ─────────────────────────────────────────────
# Split into premise/books, per-character arcs, and themes/quotes so
# build_series_context() can compose only what the content type actually needs.

_GL_PREMISE = """=== THE GUARDIAN LEAGUE (Urban Fantasy — Earth, present day) ===

PREMISE: Alien creatures called "the Infected" invade Earth through The Palace, a massive
Manhattan skyscraper. An unlikely found-family of humans and fantasy creatures secretly
defend the planet. They become publicly known as the Guardian League.

BOOK 1 — THE GUARDIAN OF THE PALACE:
Red (Ms. Hernandez), a former military woman turned security manager at The Palace — a massive
vertical city built across Manhattan blocks — discovers creatures from another world infiltrating
the building. She is practical, guarded, self-reliant. Her life is "foldable" — she owns almost
nothing and prefers it that way. She meets Galad (15,000-year-old elf, golden skin and eyes,
ancient calm, arrogant, initially shallow but grows to love humans),
Grundle (massive heroic troll, war axe, surprisingly gentle), and Harry
(dwarf, former actor, theatrical, fascinated by computers). Together they form the core of the Guardian League.
The Infected are a hive-like magical threat from another world.

BOOK 2 — STARS IN THE SAND:
The team goes international, and the interworld. The FBI is now aware of the alien situation. Rocks (a one-legged
former military contact with the magic to create illusions) becomes central.
High stakes political fallout, imprisoned mages, and the team's bond deepening under pressure.
New recruits join the magical team with Talents that mimic super-heroes.

BOOK 3 — WE'RE GOING ON AN ELF HUNT:
The team expands. Mort (ancient, robed warrior who displays Infected heads on a staff as trophies)
and Hirashi join. A character named Scan grows Rock's leg back. Scan has a mysterious power to
alter physiology (more than just Healing). Red and Galad's relationship deepens.
Ends with warmth amid chaos — Galad returning, the team whole again.

BOOK 4 — THE SONG UNSUNG:
The Infected threat peaks. An Illusionist who can impersonate anyone — possibly invisibly —
creates a new layer of paranoia. The team debates killing a character who may be their only
chance to understand the enemy. Grundle's defining line: "He is my friend. Make no mistake."
Resolution requires cross-species cooperation and a deeper grasp of the Infected's nature."""

_GL_CHAR_ARCS = {
    "Red": """Red Hernandez:
  Core Identity: Red begins as a hyper-competent, emotionally guarded former special-operations soldier trying to build a civilian life in Manhattan while managing security for The Palace. She defines herself by discipline, responsibility, and distance. Civilian softness unsettles her.
  Arc: Across the series, Red transforms from a lone operator who insists on control into a leader who accepts partnership, vulnerability, and even love. The invasion forces her back into combat, but this time she chooses it rather than being assigned it. She grows from reactive defender to proactive guardian — not just of buildings, but of worlds. Her relationship with Galad softens her without weakening her; instead, it integrates her military precision with emotional depth. By The Song Unsung, she is no longer trying to build a foldable life — she is building something permanent, chosen, and shared.
  Thematic Movement: Isolation → Trust → Chosen Responsibility → Love integrated with strength.""",

    "Galad": """Galad (Galadrindor Arafaemiel Terebra'an):
  Core Identity: An ancient elven Empath burdened by exile, guilt, and political catastrophe. Galad carries millennia of regret and the weight of elven collapse. He is powerful, restrained, and deeply self-critical.
  Arc: Galad begins as a Banished relic of a broken elven world, haunted by past failures and the chaos tied to his disappearance. On Earth, he finds something he never expected: moral clarity and human stubbornness. Through Red and the Guardian League, he reclaims purpose not as a ruler or symbol, but as a partner and protector. He shifts from carrying history's shame to choosing present action. By the later books, he no longer seeks redemption through grand sacrifice — he seeks it through building and protecting something that matters now.
  Thematic Movement: Exile → Redemption → Partnership → Present-tense purpose.""",

    "Grundle": """Grundle:
  Core Identity: A troll warrior of immense strength and surprisingly gentle moral clarity. Grounded, literal, and honorable. His physical presence is imposing; his emotional core is steady.
  Arc: Grundle begins as an outsider in multiple senses: alien, large, socially awkward among humans. Yet he consistently demonstrates moral steadiness and loyalty. Where elves wrestle with politics and humans with ego, Grundle often sees plainly. Over time, he becomes not just muscle but emotional ballast for the team. His relationship with Smith deepens him, revealing vulnerability beneath the stone. He grows from lone troll survivor to chosen member of a cross-world family — proving that "monster" is a matter of perspective.
  Thematic Movement: Outsider → Trusted Ally → Emotional Anchor → Found Family.""",

    "Harry": """Harry:
  Core Identity: Harry is bold, brash, and theatrically confident — a showman-warrior whose bravado masks a need for recognition. He enjoys spectacle and thrives in high-stakes chaos.
  Arc: Harry begins as a swaggering presence, relishing stories of danger and heroic flourishes. Yet beneath the showmanship lies insecurity about belonging and relevance. As the stakes rise from building defense to planetary survival, Harry gradually matures. His heroics shift from performative to purposeful. By the later books, he is still dramatic — but he fights not for applause, but because it is necessary. He becomes dependable without losing flair.
  Thematic Movement: Performance → Commitment → Earned Belonging → Courage without audience.""",

    "Scan": """Scan (Stan):
  Core Identity: Scan begins as the team's techno-savant — a hacker, systems architect, and magical pattern-reader who prefers code to conversation. Brilliant, sarcastic, and slightly socially off-beat, he hides anxiety and loyalty beneath humor and deflection.
  Arc: At the start of the series, Scan operates as the quiet enabler — breaking firewalls, designing infrastructure, and solving problems before others know they exist. The alien incursion forces him out of digital abstraction and into magical innovation. Over time, Scan evolves from hacker to architect — not just of code, but of interplanetary infrastructure. By The Song Unsung, he is no longer just the guy who can break in — he is the one who builds what comes next.
  Thematic Movement: Outsider genius → Tactical enabler → Magical systems architect → Co-creator of a new paradigm.""",

    "Rocks": """Rocks:
  Core Identity: Rocks is steady, pragmatic, and fiercely loyal — the grounded counterweight to the magic and chaos surrounding The Palace. He isn't flashy, ancient, or theatrical; his strength lies in reliability, physical courage, and an unshakable sense of responsibility.
  Arc: Rocks begins as Red's trusted second — dependable muscle and operational backbone, content to work without spotlight or credit. As the conflict widens from local security to interplanetary war, he refuses to be left behind or reduced to "just human." He adapts, learns, and steps into harder choices. By the later books, he is not merely assisting the guardians — he is one, choosing the fight not because he must, but because standing firm is who he is.
  Thematic Movement: Steadfast Support → Chosen Agency → Quiet Leadership → Loyalty as Strength.""",
}

_GL_SHARED_ARC = """Across all characters, The Guardian League traces a shared arc:
From isolation (personal or planetary) → To reluctant alliance → To chosen interdependence → To guardianship of something larger than themselves"""

_GL_THEMES_QUOTES = """THEMES — GUARDIAN LEAGUE: Found family, monster-as-hero, ordinary humans rising to extraordinary
circumstances, the cost of loyalty, humor as survival, alien invasion with real emotional stakes.

KEY QUOTES — GUARDIAN LEAGUE:
- "My entire life was foldable." (Red, Book 1 — her minimalism, her armor)
- "He is my friend. Make no mistake." (Grundle, Book 4 — defending someone others would sacrifice)"""

# ─────────────────────────────────────────────────────────────────────────────

_TR_PREMISE = """=== THAUMATROPIC ROOTS (Epic Fantasy — another world, centuries before Guardian League) ===

PREMISE: Set on Elliah's world, this prequel explores the origins of magic as known in Guardian
League, the history of elves, trolls, and dragons, and the ancient events that shaped the
Guardian League universe. Magic is as natural as breathing — except for Elliah, who was born
without a single spark.

THE WORLD: Multiple elf races — Wood Elves, High Elves, Alluvium, Salts, Warders.
"Salts for peace, Alluvium for protection. Wood Elves, life and beauty; Warders for Truth;
High Elves for solving problems." The Father of Stones controls the trolls, making war on elves.
The Mother of Trees is a dying god-like being — enormous, wooden, weeping — whose visions
of the future drive the series' prophecy engine. Dragons are intelligent, proud, and telepathic.

BOOK 1 — MOTHER OF TREES:
Elliah is born without magic in a world where magic is everything. The Mother of Trees holds her
as a newborn and Sees that Elliah's thread passes through the End of the world — impossible.
Elliah grows up quick and clever, more comfortable in trees than with people. She meets Hughelas
(Wood Elf, lightning magic, funny and warm) and Beldroth (Warder warrior, quiet and steady).
Recruited into a war despite having no magic. Her weapon: observation, will, and refusal to
accept the limits others set. The Mother of Trees laughs and sobs at what she Sees in Elliah. Zoras
(morally complex antagonist) is central.

BOOK 2 — BONES OF CENAEDTH:
The group travels to Alenor — the High Elf city with eerie stone tree simulacrums. From there,
they go to Cenaedth, to recruit the Alluvium to once again join the fight against the trolls.
Elliah grows from clever survivor into strategic force. They stave off a red dragon attack on
Cenaedth, and Elliah helps solve the mystery of their young Bereft dying. Dragon bones keep the
babies alive. The Alluvium join the fight and send forces to the war front. Trentius (Hook-damaged
High Elf mind, accidentally brilliant, reader favorite) appears.
A dragon named Smoky is accidentally Compelled into friendship.

BOOK 3 — SECRETS OF DEARA:
Deep lore on the Father of Stones, and cross-world connections.
After the upheaval in Cenaedth, Hughelas is taken by the Salts to Deara, a storm-shielded island
whose politics are as layered as its defenses. Elliah and the others follow, stepping into a
struggle between Peacekeepers, traders, and regents who each believe they alone can secure their
people's future. Within Deara's shield lie ancient artifacts, bound storm elementals, and
dangerous experiments that push magic toward collapse. By the end, the Salts commit to the
continental war, opening the path for every elven race to stand together against the trolls.

BOOK 4 — SHEPHERDS OF TRUTH (releasing April 13, 2026):
The war converges. All elven races gather for the first time since the Breaking.
The Prologue: a troll Clan Chief sacrifices his life to save his son — one of the most
emotionally powerful openings in the series. Elliah and Beldroth negotiate with the Warder
council (the Lithos Sinod) in Alenor's Luminarium to unify all races against the trolls.
Hughelas masters Teleportation using dragon teeth as anchor points. Lairras the ancient dragon
waits outside Alenor, blocking the High Elves' path — "Once, they were mine. I taught them
restraint. They have forgotten." Illiara (Elliah's mother, now visibly pregnant) refuses to
be sidelined: "I would not be sidelined. I set my feet more firmly against the court stone."
Flurry seeks her mother's bones. The stakes are real — the final convergence of all
forces that will determine whether everyone on the planet dies inside a magical cage."""

_TR_CHARS = {
    "Elliah": """Elliah:
  Born without magic. Fierce, steady, refuses to be defined by what she lacks. Her weapon is
  observation, will, and refusal to accept imposed limits. In Book 4: "There was a steadiness
  in her gaze since Deara, like she'd become an anchor while the rest of us drifted... something
  in her eyes reminded me she didn't belong to anyone — not even me — and somehow I loved her
  more for it." (Hughelas about Elliah)""",

    "Hughelas": """Hughelas:
  Wood Elf, lightning magic, warm and funny. Learning Teleportation in Book 4 using dragon teeth
  as anchors. Deeply in love with Elliah. His humor keeps the group human amid cosmic stakes.
  "Not yet. This spell's mine to try alone." """,

    "Beldroth": """Beldroth:
  Warder warrior. Massive, quiet, steady. Permanently hearing-damaged from Deara. Adapts without
  complaint. Elliah's partner. "Straight-backed, neither hurried nor slow." """,

    "Illiara": """Illiara:
  Elliah's mother. Fierce, politically shrewd, pregnant starting in Book 1 but near-term in Book 4.
  Refuses sidelines: "I would not be sidelined. I set my feet more firmly against the court stone." """,

    "Trentius": """Trentius:
  Hook-damaged High Elf. Accidentally brilliant. Reader favorite. His catchphrase-style line:
  "Spell Slipup Sparks Serendipitous Success." Endearingly oblivious.""",
}

# Per-character quote blocks for TR (used in character_spotlight to give only relevant quotes)
_TR_CHAR_QUOTES = {
    "Elliah": """- "No. I won't keep running. There's got to be a way to fight this." (Elliah, Book 1 — refusing to flee, choosing to stand)
- "None of you will let Hughelas discuss what he figured out. But he thinks he understands why I'm Bereft, and, speaking as the most freakish oddity in the room, I'd like to hear more." (Elliah, Book 3 — owning her difference with dry humor)
- "You're going to live, Hughelas Do'wood. You've got too much left to do." (Elliah, Book 4 — before his first solo teleport attempt)
- "We've come to speak with your elders. About the alliances… about what's coming." (Elliah, Book 4 — arriving at the Warder capital)""",

    "Hughelas": """- "Luckily, we have you." (Hughelas, Book 1 — after Elliah saves the group from basilisks)
- "Certain spells need boundaries, containment, to be useful. Unbounded, there's no gain to the species." (Hughelas, Book 1)
- "Not yet. This spell's mine to try alone." (Hughelas, Book 4 — before his first teleport)""",

    "Beldroth": """- "Peace and prosperity have broken out like a plague." (Beldroth, Book 4 — an observation on the silence from troll country)
- "I am Beldroth, little princess. My son tells me you and he are friends." (Beldroth, Book 1 — first meeting Elliah)
- "The Mother said she would live." (Beldroth, Book 2 — steady faith amid Illiara's fear for Elliah)
- "I don't have time for games." (Beldroth, Book 3 — low and dangerous in a Deara tavern)
- "Straight-backed, neither hurried nor slow." (narrator description of Beldroth, Book 4 — his defining physical presence)""",

    "Illiara": """- "Go through your exercises. They won't throw stones… but you might wish that's what they'd done." (Illiara, Book 2 — warning Elliah about High Elf mind magic in Alenor)
- "I would not be sidelined. I set my feet more firmly against the court stone. Bellon or worse, I would meet it standing." (Illiara, Book 4 — refusing to be left behind while visibly pregnant- not an actual quote but rather her thoughts)
- "If you do not claim the border, someone else will. And when they do, it will not stop at the border. It will leak inward—through trade, through minds, through the quiet routes your patrols do not bother to walk because you assume they remain yours." (Illiara, Book 4 — political speech to the Wood Elf council)""",

    "Trentius": """- "Spell Slipup Sparks Serendipitous Success." (Trentius, Book 3 — after accidentally Compelling Smoky)
- "She was lonely in a way… one of many, all alike. But now she's special." (Trentius, Book 3 — on Smoky)
- "Swift Strike Stops Sinister Scheme." (Trentius, Book 3)""",
}

_TR_ALL_QUOTES = """KEY QUOTES — THAUMATROPIC ROOTS:

ELLIAH:
- "No. I won't keep running. There's got to be a way to fight this." (Elliah, Book 1 — refusing to flee, choosing to stand)
- "None of you will let Hughelas discuss what he figured out. But he thinks he understands why I'm Bereft, and, speaking as the most freakish oddity in the room, I'd like to hear more." (Elliah, Book 3 — owning her difference with dry humor)
- "You're going to live, Hughelas Do'wood. You've got too much left to do." (Elliah, Book 4 — before his first solo teleport attempt)
- "We've come to speak with your elders. About the alliances… about what's coming." (Elliah, Book 4 — arriving at the Warder capital)

HUGHELAS:
- "Luckily, we have you." (Hughelas, Book 1 — after Elliah saves the group from basilisks)
- "Certain spells need boundaries, containment, to be useful. Unbounded, there's no gain to the species." (Hughelas, Book 1)
- "Not yet. This spell's mine to try alone." (Hughelas, Book 4 — before his first teleport)

BELDROTH:
- "Peace and prosperity have broken out like a plague." (Beldroth, Book 4 — an observation on the silence from troll country)
- "I am Beldroth, little princess. My son tells me you and he are friends." (Beldroth, Book 1 — first meeting Elliah)
- "The Mother said she would live." (Beldroth, Book 2 — steady faith amid Illiara's fear for Elliah)
- "I don't have time for games." (Beldroth, Book 3 — low and dangerous in a Deara tavern)
- "Straight-backed, neither hurried nor slow." (narrator description of Beldroth, Book 4 — his defining physical presence)

ILLIARA:
- "Go through your exercises. They won't throw stones… but you might wish that's what they'd done." (Illiara, Book 2 — warning Elliah about High Elf mind magic in Alenor)
- "I would not be sidelined. I set my feet more firmly against the court stone. Bellon or worse, I would meet it standing." (Illiara, Book 4 — refusing to be left behind while visibly pregnant- not an actual quote but rather her thoughts)
- "If you do not claim the border, someone else will. And when they do, it will not stop at the border. It will leak inward—through trade, through minds, through the quiet routes your patrols do not bother to walk because you assume they remain yours." (Illiara, Book 4 — political speech to the Wood Elf council)

SECONDARY CHARACTERS:
- "Salts for peace, Alluvium for protection. Wood Elves, life and beauty; Warders for Truth; High Elves for solving problems." (the race taxonomy — Book 1)
- "By all that's green and growing, name her!" (The Mother of Trees, Book 1 — on Elliah as a newborn)
- "Everyone but her. She will be here with me. I Saw that. The rest of you, everyone here, dies. I'm so sorry." (The Mother of Trees, Book 1 — her Blessing to Beldroth)
- "Once, they were mine. The Mother placed High Elves under my keeping when their magic was young and unsteady. I taught them restraint. They have forgotten." (Lairras, Book 4)
- "I seek redemption." (Zoras, Book 1)
- "The Mother enjoyed the stories we devised. She said they sounded so much more brilliant than reality." (Zoras, Book 1 — on creation mythology)
- "Do you destroy all the bricks in your kiln when but one shatters? You condemn them as a race for condemning us as a race." (Wynruil, Book 2 — to Gormar, defending the High Elves)
- "Elven magic grows stronger with each generation. But the trolls' resistance to magic grows as well. And they breed faster. That… is why we will lose." (Wynruil, Book 1 — the war in one bleak summary)
- "Spell Slipup Sparks Serendipitous Success." (Trentius, Book 3 — after accidentally Compelling Smoky)
- "She was lonely in a way… one of many, all alike. But now she's special." (Trentius, Book 3 — on Smoky)
- "Swift Strike Stops Sinister Scheme." (Trentius, Book 3)"""

SERIES_CONTEXT_CONNECTION = """
CONNECTION BETWEEN SERIES: The events of Thaumatropic Roots directly affect magic as it is known
in the Guardian League books. Elliah connects both worlds. Reading both series reveals layers
invisible in either alone."""

# Full composite constants (used for series_recap and any unrecognised content type)
SERIES_CONTEXT_GL = (
    _GL_PREMISE
    + "\n\nKEY CHARACTERS — GUARDIAN LEAGUE:\n"
    + "\n\n".join(_GL_CHAR_ARCS.values())
    + "\n\n" + _GL_SHARED_ARC
    + "\n\n" + _GL_THEMES_QUOTES
)

SERIES_CONTEXT_TR = (
    _TR_PREMISE
    + "\n\nKEY CHARACTERS — THAUMATROPIC ROOTS:\n"
    + "\n\n".join(_TR_CHARS.values())
    + "\n\n" + _TR_ALL_QUOTES
)


# Content-type groups used by build_series_context.
# These are string literals matching the content type names used across channels.
_AUTHOR_ONLY_TYPES = {"behind_the_scenes"}
_CAMPAIGN_MINIMAL_TYPES = {"countdown", "cover_feature", "release_day", "post_launch"}
_THEMES_ONLY_TYPES = {"quote_graphic", "trope_post", "moodboard_carousel", "world_building"}


def build_series_context(series, content_type="", spotlight_subject=None):
    """Return only the series context sections needed for content_type + subject.

    Keeps token counts low by omitting character arc paragraphs for types that
    don't need them (behind_the_scenes, campaign posts, trope/moodboard/world posts)
    and by including only the ONE featured character's arc for character_spotlight.
    """
    # behind_the_scenes: author voice only — no series lore needed
    if content_type in _AUTHOR_ONLY_TYPES:
        return AUTHOR_BIO

    # Campaign posts: minimal context — just premise + book titles
    if content_type in _CAMPAIGN_MINIMAL_TYPES:
        if series == "guardian_league":
            return AUTHOR_BIO + "\n" + _GL_PREMISE
        elif series == "thaumatropic_roots":
            return AUTHOR_BIO + "\n" + _TR_PREMISE
        else:
            return AUTHOR_BIO + "\n" + _GL_PREMISE + "\n" + _TR_PREMISE + SERIES_CONTEXT_CONNECTION

    # character_spotlight: premise + only the featured character's arc + their quotes
    if content_type == "character_spotlight" and spotlight_subject:
        if series == "guardian_league":
            char_arc = _GL_CHAR_ARCS.get(spotlight_subject)
            if char_arc:
                return (
                    AUTHOR_BIO + "\n" + _GL_PREMISE
                    + "\n\nKEY CHARACTER:\n" + char_arc
                    + "\n\n" + _GL_SHARED_ARC
                    + "\n\n" + _GL_THEMES_QUOTES
                )
        elif series == "thaumatropic_roots":
            char_info = _TR_CHARS.get(spotlight_subject)
            if char_info:
                char_quotes = _TR_CHAR_QUOTES.get(spotlight_subject, "")
                ctx = AUTHOR_BIO + "\n" + _TR_PREMISE + "\n\nKEY CHARACTER:\n" + char_info
                if char_quotes:
                    ctx += "\n\nKEY QUOTES — " + spotlight_subject.upper() + ":\n" + char_quotes
                return ctx
        # Unknown subject (custom override) — fall through to full context below

    # Trope, moodboard, world_building, quote_graphic: premise + themes/quotes, no char arcs
    if content_type in _THEMES_ONLY_TYPES:
        if series == "guardian_league":
            return AUTHOR_BIO + "\n" + _GL_PREMISE + "\n\n" + _GL_THEMES_QUOTES
        elif series == "thaumatropic_roots":
            return AUTHOR_BIO + "\n" + _TR_PREMISE + "\n\n" + _TR_ALL_QUOTES
        else:
            return (
                AUTHOR_BIO + "\n" + _GL_PREMISE + "\n\n" + _GL_THEMES_QUOTES
                + "\n" + _TR_PREMISE + "\n\n" + _TR_ALL_QUOTES
                + SERIES_CONTEXT_CONNECTION
            )

    # Default (series_recap, unknown types): full context
    if series == "guardian_league":
        return AUTHOR_BIO + "\n" + SERIES_CONTEXT_GL
    elif series == "thaumatropic_roots":
        return AUTHOR_BIO + "\n" + SERIES_CONTEXT_TR
    else:
        return AUTHOR_BIO + "\n" + SERIES_CONTEXT_GL + "\n" + SERIES_CONTEXT_TR + SERIES_CONTEXT_CONNECTION
