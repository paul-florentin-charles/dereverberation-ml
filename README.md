## Requirements

- Python 3.x
- Pip 3.x
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
python3 main.py path/to/dry/signals/dir path/to/impulse/responses/dir path/to/output/dir
```

or as a script

```bash
chmod 744 main.py
./main.py path/to/dry/signals/dir path/to/impulse/responses/dir path/to/output/dir
```

information will be stored in a JSON file whose name is set in **config.toml**

## Demo

```bash
make demo
```

you can change the demo size by modifying the field *size* in section *demo* in **config.toml**

possible values are :
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

note that this will remove *_\_pycache__* directories, possibly slowing down next use

## JSON Syntax

```json
{
	"drypath0": "wetdirpath0",
	"drypath1": "wetdirpath1",
	"drypath2": "wetdirpath2",
	...
}
```

each path to a dry signal is a key to the directory path that contains all of its wet samples
