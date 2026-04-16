"""
image_guidance.py
Midjourney image prompt rules shared across all content channels.
"""

MJ_IMAGE_PROMPT_GUIDANCE = """
IMAGE PROMPT RULES (Midjourney-compatible — follow exactly):
- Format: comma-separated descriptors, NOT prose sentences
- Structure per prompt: [subject/scene], [medium/art style], [lighting], [color palette], [mood]
- Recommended art styles: "dark fantasy concept art", "fantasy illustration", "digital painting",
  "cinematic concept art", "atmospheric fantasy art", "moody ink illustration"
- Lighting keywords: "volumetric lighting", "dramatic rim lighting", "golden hour light",
  "magical glowing light", "deep shadows with highlights", "dappled forest light", "backlit silhouette"
- NEVER include text, letters, words, signs, or written language in the image
- NEVER depict faces or portraits directly — use silhouettes, backs of figures, obscured profiles,
  hands gripping weapons/objects, wide environmental shots with distant figures, or close-ups of
  meaningful objects (a sword, a staff, ancient stone, glowing runes, forest canopy)
- Each prompt must describe ONE strong focused visual — avoid busy multi-character action scenes
- Hero image (first in image_prompts, or the single image_prompt) must end with --ar 9:16"""
