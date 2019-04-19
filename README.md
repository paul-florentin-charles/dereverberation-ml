# Requirements

Mandatory
- Python 3 (tested for 3.5 and 3.7)
- PyPI: Python Package Index

Optional
- GNU Make

# Get started

```bash
git clone https://gitgud.io/polochinoc/dereverberation-ml.git
cd dereverberation-ml
make install
make demo
```

if you don't have make

```bash
git clone https://gitgud.io/polochinoc/dereverberation-ml.git
cd dereverberation-ml
sudo pip3 install -r requirements.txt
python3 demo.py
```

# Instructions

## Install

```bash
make install
```

equivalent to

```bash
sudo pip3 install -r requirements.txt
```

## Run

```bash
make run dry=path/to/dry/signals/dir fx=path/to/impulse/response [wet=path/to/output/dir]
```

equivalent to

```bash
python3 main.py path/to/dry/signals/dir path/to/impulse/response [path/to/output/dir]
```

Information will be stored in a JSON file whose name is set in **config.toml**.

Retrieved data is also directly saved in an *.npz* file, whose name can be change in *data.numpy* section of **config.toml**.

## Demo

```bash
make demo
```

equivalent to

```bash
python3 demo.py
```

You can change demo urls by modifying fields in *demo.urls* section in **config.toml** ; *dry* field concerns the dataset of dry samples, and *fx* designates the fx sample.

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

This will remove all extra files generated while running main script or demo, apart from *model* directory specified in *neuralnet.dnames* section, since it contains very time-consuming files to generate.

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
	"drypath0": "wetpath0",
	"drypath1": "wetpath1",
	"drypath2": "wetpath2",
	...
}
```

Each path to a dry signal is a key to its corresponding wet signal.

## Model

Models are stored in directory written in **config.toml** at *neuralnet.dnames* section, field *model*.

The syntax for model's names is the following:

**model.{epoch:XX}-{val_loss:X.XXX}.h5**

*epoch* is the current epoch written using two digits, while *val_loss* is the validation loss written using three decimals.