IMPORTANT_BEAR_LIST = {
    'All': {'FilenameBear', 'InvalidLinkBear', 'LineCountBear'},
    'C': {'GNUIndentBear', 'CSecurityBear', 'ClangComplexityBear'},
    'C#': {'CPDBear', 'CSharpLintBear', 'SpaceConsistencyBear'},
    'C++': {'GNUIndentBear', 'CPDBear', 'CPPCheckBear', 'CPPCleanBear',
            'ClangComplexityBear'},
    'CMake': {'CMakeLintBear', 'SpaceConsistencyBear'},
    'CSS': {'CSSLintBear', 'SpaceConsistencyBear'},
    'JavaScript': {'JSHintBear', 'JSComplexityBear'},
    'Java': {'JavaPMD', 'CheckstyleBear'},
    'Python': {'PycodestyleBear'}}

# This includes the bears from IMPORTANT_BEAR_LIST
GREEN_MODE_COMPATIBLE_BEAR_LIST = {}

# This takes precedence over the other two bear lists.
GREEN_MODE_INCOMPATIBLE_BEAR_LIST = {
    'FilenameBear',
    }

ALL_CAPABILITIES = {
    'Code Simplification',
    'Commented Code',
    'Complexity',
    'Documentation',
    'Duplication',
    'Formatting',
    'Grammar',
    'Memory Leak',
    'Missing Import',
    'Redundancy',
    'Security',
    'Smell',
    'Spelling',
    'Syntax',
    'Undefined Element',
    'Unreachable Code',
    'Unused Code',
    'Variable Misuse'
}

DEFAULT_CAPABILITIES = {
    'Syntax',
    'Formatting',
    'Documentation',
    'Redundancy',
    'Spelling',
    'Smell',
    'Code Simplification',
    'Complexity',
}

HASHBANG_REGEX = '(^#!(.*))'

ASK_TO_SELECT_LANG = ('Which languages would you like to generate a config '
                      'file for?\n'
                      'Please select some languages using '
                      'their numbers or just press \'Enter\' to select '
                      'all of them\n')
