{
  'targets': [
    {
      'target_name': 'googlemock',
      'type': 'static_library',
      'include_dirs': [
        '.',
        'include',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '.',
          'include',
        ],
      },
      'sources': [
        'include/gmock/gmock.h',
        'include/gmock/gmock-actions.h',
        'include/gmock/gmock-cardinalities.h',
        'include/gmock/gmock-generated-actions.h',
        'include/gmock/gmock-generated-actions.h.pump',
        'include/gmock/gmock-generated-function-mockers.h',
        'include/gmock/gmock-generated-function-mockers.h.pump',
        'include/gmock/gmock-generated-matchers.h',
        'include/gmock/gmock-generated-matchers.h.pump',
        'include/gmock/gmock-generated-nice-strict.h',
        'include/gmock/gmock-generated-nice-strict.h.pump',
        'include/gmock/gmock-matchers.h',
        'include/gmock/gmock-more-actions.h',
        'include/gmock/gmock-more-matchers.h',
        'include/gmock/gmock-spec-builders.h',
        'include/gmock/internal/gmock-generated-internal-utils.h',
        'include/gmock/internal/gmock-generated-internal-utils.h.pump',
        'include/gmock/internal/gmock-internal-utils.h',
        'include/gmock/internal/gmock-port.h',
        'src/gmock-all.cc',
        'src/gmock-internal-utils.cc',
        'src/gmock-spec-builders.cc',
        'src/gmock_main.cc',
        'src/gmock-cardinalities.cc',
        'src/gmock-matchers.cc',
        'src/gmock.cc',
      ],
      'dependencies': [
        '../googletest/googletest.gyp:googletest',
      ],
    },
  ],
}
