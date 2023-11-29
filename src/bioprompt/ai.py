from marvin import AIApplication

from bioprompt.prompts.system import BioPromptSystem, FixesSystem
from bioprompt.tools.align import align_sequence
from bioprompt.tools.revcomp import reverse_compliment

bp = AIApplication(
    name="bioprompt",
    description=BioPromptSystem().content,
    additional_prompts=[FixesSystem()],
    tools=[align_sequence, reverse_compliment],
)
