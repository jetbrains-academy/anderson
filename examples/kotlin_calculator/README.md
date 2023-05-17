# Kotlin calculator

This is a simple Kotlin calculator.

Run the following command to generate GIFs:

```bash
anderson "kotlinc Main.kt -include-runtime -d /tmp/Main.jar && java -jar /tmp/Main.jar" ./gifs ./config.yaml
```

**Note**: You need to have the `JetBrains Mono` font in your system in order for the GIFs to be generated.
You can download the font [here](https://www.jetbrains.com/lp/mono/).
You can also change the font in the config to any other font that is installed in your system.

In the `gifs` folder you will get the following gifs:

| `light.gif`                    | `dark.gif`                   |
|--------------------------------|------------------------------|
| ![light.gif](gifs%2Flight.gif) | ![dark.gif](gifs%2Fdark.gif) |
