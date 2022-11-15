import re

from .promptgenerator import PromptGenerator

re_wildcard = re.compile(r"__(.*?)__")

# regex for solo Dynamic Prompt - incompatible with Jinja scripting
#re_combinations = re.compile(r"\{([^{}]*)}")
# ~~jinja uses {# #} and {% %} so forbid parsing # and % inside of {}~~
# but that breaks Jinja scripting in Dynamic Templates, something is/isn't parsed that should be
# so switch Dynamic Prompt to use <> instead of {} - this Dynamic Prompt regex <||> now ignores Jinja scripts {{}} {##} {%%} 
re_combinations = re.compile(r"<([^<>]*)>")

from .randomprompt import RandomPromptGenerator
from .combinatorial import CombinatorialPromptGenerator
from .magicprompt import MagicPromptGenerator
from .batched_combinatorial import BatchedCombinatorialPromptGenerator
from .feelinglucky import FeelingLuckyGenerator