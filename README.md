# NI-HSDIO Python Wrapper

A Python ctypes wrapper for the NI-HSDIO driver (`niHSDIO_64.dll`), auto-generated using [ctypesgen](https://github.com/ctypesgen/ctypesgen). This provides direct access to the NI-HSDIO C API from Python for controlling NI High-Speed Digital I/O hardware.

## Prerequisites

- Latest **NI-HSDIO driver** installed (includes `niHSDIO_64.dll`)
- **Python 3.6+** (64-bit)

## How this wrapper was Generated

The wrapper was generated from the NI-HSDIO C header using `ctypesgen`:

```
pip install ctypesgen
```

```
ctypesgen -l niHSDIO_64 -o niHSDIO_64.py "C:\Program Files (x86)\IVI Foundation\IVI\Include\niHSDIO.h" -I "C:\Program Files (x86)\IVI Foundation\IVI\Include"
```

This reads the `niHSDIO.h` header and produces a Python module that loads the DLL at import time and exposes all functions, constants, and type aliases via `ctypes`.

## Usage

Simply download the `niHSDIO_64.py` and place it next to your python script and import the module like this:

```python
from niHSDIO_64 import *
```

The standard C examples installed with the NI-HSDIO driver are a great reference for implementing your Python scripts. The function calls and flow translate directly — just use the Python wrapper equivalents. These examples are typically found at:

```
C:\Users\Public\Documents\National Instruments\NI-HSDIO\Examples\c
```

#### Using a Coding Agent to Convert C Examples

You can use an AI coding agent (e.g. GitHub Copilot) to quickly convert any NI-HSDIO C example to Python using this wrapper. Here's an example prompt you can use:

> Convert the NI-HSDIO C example at `C:\Users\Public\Documents\National Instruments\NI-HSDIO\Examples\c\Static\StaticGeneration\StaticGeneration.c` to a Python script using the `niHSDIO_64.py` ctypes wrapper. All NI-HSDIO function calls map 1:1 from C to Python. Use `ctypes.byref()` for output pointer parameters, and remember that all string arguments (resource names, channel lists, etc.) must be byte strings (`b"..."`). Convert the `checkErr` macro to a `raise_on_error` helper that checks the return status and raises an exception including the error code and description from `niHSDIO_GetError`.

You can substitute the path with any other C example from the examples directory. The agent will read the C source and produce an equivalent Python script using this wrapper.

### Example: Static Generation (converted from C example)

The following Python script is a direct conversion of `C:\Users\Public\Documents\National Instruments\NI-HSDIO\Examples\c\Static\StaticGeneration\StaticGeneration.c`:

```python
"""
Static Generation Example
  Generates static data on specified channels.
  Converted from the NI-HSDIO C example: StaticGeneration.c
"""

from niHSDIO_64 import *
from ctypes import byref


def raise_on_error(session, error_code):
    """Equivalent of checkErr in the C examples. Raises if error_code != 0."""
    if error_code != VI_SUCCESS:
        err_code = ViStatus(error_code)
        err_desc = (ViChar * 1024)()
        niHSDIO_GetError(session, byref(err_code), 1024, err_desc)
        raise RuntimeError(
            f"NI-HSDIO error {error_code}: {err_desc.value.decode()}")


# --- Configuration ---
device_id = b"PXI1Slot2"      # byte string required for C string params
channel_list = b"0-15"
write_data = 0x4321
channel_mask = 0xFFFF          # all channels

vi = ViSession()

try:
    # Initialize generation session
    raise_on_error(vi, niHSDIO_InitGenerationSession(
        device_id, VI_FALSE, VI_FALSE, None, byref(vi)))

    # Assign channels for static generation
    raise_on_error(vi, niHSDIO_AssignStaticChannels(vi, channel_list))

    # Write static data with channel mask
    raise_on_error(vi, niHSDIO_WriteStaticU32(vi, write_data, channel_mask))

    print("Done without error.")

except RuntimeError as e:
    print(f"\nError encountered\n===================\n{e}")

finally:
    # Close the session
    niHSDIO_close(vi)
```

## Common Pitfall: Byte Strings

The NI-HSDIO C API uses C strings (`char*`) for resource names, channel lists, trigger sources, waveform names, etc. In Python 3, these must be passed as **byte strings** (`b"..."`) rather than regular strings (`"..."`).

```python
# WRONG - will cause unexpacted results
niHSDIO_InitGenerationSession("Dev1", ...)
niHSDIO_AssignDynamicChannels(session, "0-3")
niHSDIO_WriteNamedWaveformU32(session, "myWaveform", ...)

# CORRECT - use byte strings
niHSDIO_InitGenerationSession(b"Dev1", ...)
niHSDIO_AssignDynamicChannels(session, b"0-3")
niHSDIO_WriteNamedWaveformU32(session, b"myWaveform", ...)
```

If you forget the `b` prefix, you will get unexpected results from the driver calls. Like as resource name is invalid error when you pass the correct resource name but forgot the `b` prefix.

**Rule of thumb:** Any string argument passed to an `niHSDIO_*` function must be a byte string.

## Key Types

| Python Alias | ctypes Type | Description |
|---|---|---|
| `ViSession` | `c_ulong` | Instrument session handle |
| `ViStatus` | `c_long` | Return status code (0 = success) |
| `ViBoolean` | `c_ushort` | Boolean (`VI_TRUE`/`VI_FALSE`) |
| `ViReal64` | `c_double` | 64-bit float |
| `ViInt32` | `c_long` | 32-bit integer |
| `ViUInt32` | `c_ulong` | 32-bit unsigned integer |
| `ViString` / `ViConstString` | `POINTER(c_char)` | C string (use byte strings) |
| `ViAttr` | `c_ulong` | Attribute ID for Get/SetAttribute |

## Key Constants

Common constants are available as module-level variables:

- **Trigger types:** `NIHSDIO_VAL_NONE`, `NIHSDIO_VAL_DIGITAL_EDGE`, `NIHSDIO_VAL_PATTERN_MATCH`, `NIHSDIO_VAL_SOFTWARE`
- **Edge types:** `NIHSDIO_VAL_RISING_EDGE`, `NIHSDIO_VAL_FALLING_EDGE`
- **Generation modes:** `NIHSDIO_VAL_WAVEFORM`, `NIHSDIO_VAL_SCRIPTED`
- **Clock sources:** `NIHSDIO_VAL_ON_BOARD_CLOCK`, `NIHSDIO_VAL_STROBE`
- **Terminal strings:** `NIHSDIO_VAL_PFI0_STR` .. `NIHSDIO_VAL_PFI7_STR`, `NIHSDIO_VAL_RTSI0_STR` .. `NIHSDIO_VAL_RTSI7_STR`
- **Attributes:** `NIHSDIO_ATTR_SAMPLE_CLOCK_RATE`, `NIHSDIO_ATTR_SAMPLE_CLOCK_SOURCE`, `NIHSDIO_ATTR_REF_CLOCK_SOURCE`, etc.

## License

See [NI software license terms](https://www.ni.com/en-us/shop/software-license-agreement.html) for the NI-HSDIO driver. The ctypesgen tool is licensed under BSD-2-Clause.