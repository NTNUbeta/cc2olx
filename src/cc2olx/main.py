import logging
import os.path
import pprint

from cc2olx.settings import collect_settings
from cc2olx import filesystem
from cc2olx import models
from cc2olx.models import Cartridge
from cc2olx.olx import olx_xml


if __name__ == '__main__':
    settings = collect_settings()
    logging.basicConfig(**settings['logging_config'])
    logger = logging.getLogger()
    workspace = settings['workspace']
    filesystem.create_directory(workspace)
    for input_file in settings['input_files']:
        cartridge = Cartridge(input_file)
        data = cartridge.load_manifest_extracted()
        pp = pprint.PrettyPrinter(indent=2, width=160)
        cartridge.normalize()
        cartridge.serialize()
        print()
        print("=" * 100)
        import json; print(json.dumps(cartridge.normalized, indent=4))
        print(olx_xml(cartridge.normalized))
