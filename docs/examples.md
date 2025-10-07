# Examples

Examples are meant to illustrate usage of `magic-flow`. They can be found [here](https://github.com/janezpodhostnik/magic-flow/tree/master/examples)

## Running The examples

In case you want to debug the examples, or you just want to see them in action you can use the following steps.

### 1. Prerequisites

- `flow-cli` for starting the emulator ([step-by-step based installation instructions based on your OS](https://github.com/onflow/flow-cli#flow-cli))
- a checkout of `magic-flow`
- python 3.9 or higher
- [poetry](https://python-poetry.org/)

The first step is to install the dependencies of `magic-flow` with **poetry**. To do this run the following command on the root of the checkout.

```sh
poetry install
```

After that start the flow emulator in **./example** directory (because that is where the `flow.json` the emulator configuration is), using:

```sh
flow emulator
```

### 2. Running examples

To run all the examples use:

`poetry run examples`

To run specific examples you can use the tag of the examples:

`poetry run examples [ExampleTag]`

e.g.:

`poetry run examples T.1. T.2. S.4.`
