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

The config file is a yaml file with 4 fields:
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
- `keystroke_delay` – Delay between each keystroke (in milliseconds). By default, `150`.
- `keystroke_std` – Standard deviation for the `keystroke_delay` (in milliseconds). By default, `60`.
- `action_delay` – Delay between each action (in milliseconds). By default, `80`.

The `gif_config` contains the following fields:
- `gifs` – List of arguments for each of the GIFs you want to generate.
- `common` – Common arguments that need to be applied when generating each of the GIFs.

**Note**: the arguments specified in the `common` have a lower priority 
than the arguments specified for each specific GIF.

The `gifs` list item consists of the following arguments:
- `name` – Name of the GIF. In the file with this name the GIF will be saved.
- `theme` – Either the name of the built-in theme or a list of colors in hexadecimal format.
  The names of the available themes are listed in the `Theme` enum-class located [here](anderson/config/choices.py).
  More information about the list of colors can be found [here](https://github.com/asciinema/agg#color-themes).
  By default, `dracula`.
- `font_family` – Name of the font family. The available values are given in the `FontFamily` enum-class located 
  [here](anderson/config/choices.py). **Note**: the selected font family must be installed on your system.
  By default, `Liberation Mono`.
- `font_size` – Font size (in pixels). By default, `14`.
- `fps_cap` – FPS cap. By default, `30`.
- `line_height` – Line height. By default, `1.4`.
- `speed` – Playback speed. By default, `1`.
- `no_loop` – Disable animation loop. By default, `false`.

There are several kinds of actions that can be present in the `scenario`:
- `enter` – Enter some string in the terminal.
- `expect` – Wait for some string in the terminal.
- `delay` – Overwrite the `keystroke_delay` argument. **Note**: the overwriting happens globally, therefore if you need 
  to change this argument for some part of the scenario, don't forget to revert to the default value.
- `wait` – Overwrite the `action_delay` argument. **Note**: the overwriting happens globally, therefore if you need to 
  change this argument for some part of the scenario, don't forget to revert to the default value.

Examples of config files you can see in the [`examples`](examples) folder.

## License

Copyright &copy; 2023 Ilya Vlasov.

All code is licensed under the Apache License, Version 2.0. See LICENSE file for details.
