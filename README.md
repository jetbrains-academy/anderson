# Anderson
Anderson is a tool for automatically recording a terminal session 
according to a given scenario into animated GIF files.

It uses:
- [`asciinema`](https://github.com/asciinema/asciinema) to record a terminal session;
- [`Asciinema-Automation`](https://github.com/PierreMarchand20/asciinema_automation) to automate asciinema recording;
- [`agg`](https://github.com/asciinema/agg) to generate animated GIF files.

## Installation

Simply run the following command:
```bash
pip install git+https://github.com/GirZ0n/anderson.git
```

## Usage

Run the tool with the several arguments:
```bash
anderson <executable> <ouput> <config> [--debug]
```
where:
- `<executable>` – Executable to record.
- `<output>` – Path where to save GIFs.
- `<config>` – Path to a config file. For more information: see [this](#config) section.

You can also specify the `--debug` flag which enables debug logging.

### Examples

Examples of using the tool are presented in the corresponding [folder](examples).

### Config

The config consists of 4 fields:
- `terminal_config` – Arguments related to the terminal where automatic interaction takes place. 
  They are passed to `ascicinema`. This field is optional.
- `interaction_config` – Arguments related to automatic interaction with the terminal. 
  They are passed to `Asciinema-Automation`. This field is optional.
- `gif_config` – Arguments related to the generation of GIFs. They are passed to `agg`.
- `scenario` – List of actions to be performed during interaction with the executable.

The `terminal_config` contains the following arguments:
- `cols` – Terminal columns. By default: `80`.
- `rows` – Terminal rows. By default: `24`.

The `interaction_config` contains the following arguments:
- `keystroke_delay` – Delay between each keystroke (in milliseconds). Be default, `150`.
- `keystroke_std` – Standard deviation for the `keystroke_delay` (in milliseconds). Be default, `60`.
- `action_delay` – Delay between each action (in milliseconds). Be default, `80`.


## License

Copyright &copy; 2023 Ilya Vlasov.

All code is licensed under the Apache License, Version 2.0. See LICENSE file for details.
