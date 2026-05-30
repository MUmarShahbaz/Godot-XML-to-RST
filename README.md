# Godot XML to RST

Stripped down variant of Godot's official XML to RST converter. The converter works exactly the same way as the official with the minor chages to CLI syntax.

## Usage

**Original Syntax**
```bash
python make_rst.py [arguments] /path/to/xml_folder
```

**New Syntax**
```bash
python convert_xml.py [internal?] [arguments] /path/to/xml_folder
```

The flag `[internal?]` is used to select whether or not the built-in variables should be included or not. It can either be `--internal` or `--no-internal`.

The `[arguments]` represents any and all arguments that can be accepted by godot's official converter.

## Alternatively

You can skip the wrapper and directly use the official converter as follows:

**Original Syntax**
```bash
python make_rst.py [arguments] /path/to/xml_folder
```

**New Syntax**
```bash
python src/make_rst.py [internal?] [arguments] /path/to/xml_folder
```