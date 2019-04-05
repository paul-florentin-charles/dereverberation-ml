## Requirements

- Python 3.x.x (Altough 3.7 is advised)
- Python3-pip x.x  
- [GNU Make x.x]
- [Curl x.x]

```bash
sudo pip3 install -r requirements.txt
```

or equivalent

```bash
make install
```

## Run

```bash
make run dry=path/to/dry/signals/dir fx=path/to/impulse/responses/dir [wet=path/to/output/dir]
```

or

```bash
python3 main.py path/to/dry/signals/dir path/to/impulse/responses/dir [path/to/output/dir]
```

or as a script

```bash
chmod 744 main.py
./main.py path/to/dry/signals/dir path/to/impulse/responses/dir [path/to/output/dir]
```

Information will be stored in a JSON file whose name is set in **config.toml**.

Retrieved data is also directly saved in an *.npz* file, whose name can be change in *data* section of **config.toml**.

## Demo

```bash
python3 demo.py
```

or if you have *Make* installed

```bash
make demo
```

You can change the demo size by modifying the field *size* in section *demo.datasets* in **config.toml**.

Possible values are:
* `tiny`
* `small`
* `medium`
* `big`

## Clean

```bash
make clean
```

or

```bash
make cleanall
```

equivalent to

```bash
python3 clean.py
```

This will remove all extra files generated while running main script or demo.

## Logging

There is a field *level* in section *logger* in **config.toml**, that is set at `debug` by default.

Possible values are:
* `debug`
* `info`
* `warning`
* `error`
* `critical`

Each value prevents lower value messages to be displayed.

For instance, if set on *warning*, *debug* and *info* messages won't be displayed.

## JSON Syntax

```json
{
	"drypath0": "wetdirpath0",
	"drypath1": "wetdirpath1",
	"drypath2": "wetdirpath2",
	...
}
```

Each path to a dry signal is a key to the directory path that contains all of its wet samples.