from robocop.formatter.disablers import skip_if_disabled
from robocop.formatter.formatters.aligners_core import AlignKeywordsTestsSection
from robocop.formatter.skip import Skip


class AlignKeywordsSection(AlignKeywordsTestsSection):
    """
    Align ``*** Keywords ***`` section to columns.

    Align keyword calls and settings into columns with predefined width. There are two possible alignment types
    (configurable via ``alignment_type``):
      - ``fixed`` (default): pad the tokens to the fixed width of the column
      - ``auto``: pad the tokens to the width of the longest token in the column

    Example output:
    ```robotframework
    *** Keywords ***
    Keyword
        ${var}        Create Resource       ${argument}       value
        Assert        value
        Multi
        ...           line
        ...           args
    ```

    Column widths can be configured via ``widths`` (default ``24``). It accepts comma separated list of column widths.

    Tokens that are longer than width of the column go into "overflow" state. It's possible to decide in this
    situation (by configuring ``handle_too_long``):
      - ``overflow`` (default): align token to the next column
      - ``compact_overflow``: try to fit next token between current (overflowed) token and the next column
      - ``ignore_rest``: ignore remaining tokens in the line
      - ``ignore_line``: ignore whole line

    It is possible to skip formatting on various types of the syntax (documentation, keyword calls with specific names
    or settings).
    """

    def __init__(
        self,
        widths: str = "",
        alignment_type: str = "fixed",
        handle_too_long: str = "overflow",
        compact_overflow_limit: int = 2,
        align_comments: bool = False,
        align_settings_separately: bool = False,
        skip_documentation: str = "True",  # noqa: ARG002 - override skip_documentation from Skip
        skip: Skip = None,
    ):
        super().__init__(
            widths,
            alignment_type,
            handle_too_long,
            compact_overflow_limit,
            align_comments,
            align_settings_separately,
            skip,
        )

    @skip_if_disabled
    def visit_Keyword(self, node):  # noqa: N802
        self.create_auto_widths_for_context(node)
        self.generic_visit(node)
        self.remove_auto_widths_for_context()
        return node

    def visit_TestCase(self, node):  # noqa: N802
        return node
