from hangar.external import BasePlugin


class Hangar{{cookiecutter.plugin_name}}(BasePlugin):
    def __init__(self):
        provides = None
        accepts = None
        super().__init__(provides, accepts)

    def load(self, fpath, **plugin_kwargs):
        """
        Docstring
        """
        raise NotImplementedError

    def save(self, arr, outdir, sample_detail, format_str, **plugin_kwargs):
        """
        Docstring
        """
        raise NotImplementedError

    def show(self, arr, **plugin_kwargs):
        """
        Docstring
        """
        raise NotImplementedError

    def board_show(self, arr, **plugin_kwargs):
        """
        Docstring
        """
        raise NotImplementedError
