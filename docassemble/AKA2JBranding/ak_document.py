import re
from docassemble.base.util import (action_button_html)

def one_file_download_html(button_htmls):
    """
    Uses the list of button html strings to
    return the row of an AL document-styled table in HTML format.
    """
    html = (
        f'\n\t<div class="row al_doc_table_row">'
        # At some widths, `col-6` barely has room to avoid
        # wrapping lines for these buttons
        f'\n\t\t<div class="col col-12 col-sm-6 al_buttons">'
    )
    for button in button_htmls:
        html += button
    html += "</div>"
    html += "\n\t</div>"

    return html

def html_safe_str(the_string: str) -> str:
    """
    Return a string that can be used as an html class or id
    """
    return re.sub(r"[^A-Za-z0-9]+", "_", the_string)
 

def download_buttons_html(
        doc,
        key: str = "preview",
        format: str = "pdf",
        pdfa: bool = False,
        view: bool = True,
        refresh: bool = True,
        view_label: str = "See PDF",
        view_icon: str = "eye",
        download_label: str = "Download",
        download_icon: str = "download",
    ) -> str:
        """
        Returns an HTML string of a table to display all the docs
        combined into one pdf with 'view' and 'download' buttons.
        """
        if format == "docx":
            the_file = doc.as_docx(key=key)
        else:
            the_file = doc.as_pdf(key=key, pdfa=pdfa)

        doc_download_button = action_button_html(
            the_file.url_for(attachment=True),
            label=download_label,
            icon=download_icon,
            color="primary",
            size="md",
            classname="al_download",
        )
        if view:
            pdf = doc.as_pdf(key=key)
            if not pdf:
                buttons = [doc_download_button]
            else:
                doc_view_button = action_button_html(
                    pdf.url_for(attachment=False),
                    label=view_label,
                    icon=view_icon,
                    color="secondary",
                    size="md",
                    classname="al_view",
                )
                buttons = [doc_view_button, doc_download_button]
        else:
            buttons = [doc_download_button]

        html = (
            f'<div class="container al_table merged_docs" id="{html_safe_str(doc.instanceName)}">'
            f"{one_file_download_html(buttons)}"
            f"\n</div>"
        )

        return html
