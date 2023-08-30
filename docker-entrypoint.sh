#!/usr/bin/env bash
python3 -m coverage run --omit=tests/* -m pytest tc_core_analyzer_lib/tests
python3 -m coverage lcov -o coverage/lcov.info