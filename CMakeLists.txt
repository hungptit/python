cmake_minimum_required(VERSION 3.10.2)
project(python_examples)

file(GLOB PY_SRCS examples/*.py)

# Lint all Python and Bash files
add_custom_command(
  OUTPUT .pylint_stamp
  DEPENDS ${PY_SRCS}
  COMMAND flake8 --filename=* ${PY_SRCS}
  COMMAND yapf -d ${PY_SRCS}
  COMMAND mypy --ignore-missing-imports --follow-imports=skip
          --check-untyped-defs ${PY_SRCS}
  COMMAND touch .pylint_stamp
  COMMENT "Lint Python files with flake8, yapf, and mypy.")
add_custom_target(lint ALL DEPENDS .pylint_stamp)

# Format all Python files
add_custom_command(
  OUTPUT .fmt_python_stamp
  DEPENDS ${PY_SRCS}
  COMMAND yapf -i ${PY_SRCS}
  COMMAND touch .fmt_python_stamp
  COMMENT "Format Python files with yapf."
  VERBATIM)

add_custom_target(
  fmt
  DEPENDS .fmt_python_stamp
  COMMENT "Format Bash, C++, CMake, and Python files.")
