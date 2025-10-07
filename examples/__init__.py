import logging.config
from pathlib import Path

import toml

import examples.account_examples
import examples.block_examples

# TODO figure out how to not need this for the _ExampleMetaClass to work correctly
import examples.client_examples
import examples.collections_examples
import examples.events_examples
import examples.generate_key
import examples.get_account_examples
import examples.scripts_examples
import examples.transactions_examples
import examples.user_message_examples  # noqa: F401

__all__ = [
    "account_examples",
    "block_examples",
    "client_examples",
    "collections_examples",
    "events_examples",
    "generate_key",
    "get_account_examples",
    "scripts_examples",
    "transactions_examples",
    "user_message_examples",
]

logging_config = toml.load(Path(__file__).parent.joinpath("./logging.toml"))
logging.config.dictConfig(logging_config)
