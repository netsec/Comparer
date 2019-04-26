# Comparer

A simple Python3 script that can be used to compare a file with the output of a system command


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

[Python3](https://docs.python-guide.org/starting/install3/linux/)

### Installing

#### Git Clone

```bash
git clone https://github.com/knadt/Comparer.git
cd Comparer
```

#### Running

```bash
python3 comparer.py -h

comparer.py -i <inputfile> -o <outputfile> -c <command>
```

## Help

comparer.py -i <inputfile> -o <outputfile> -c <command>')
  
  -h help
  -i (ifile=''): initial file to compare cmd to
  -o (ofile=''): output of command to be saved to file (tmp file)
  -c (cmd='')  : system command
  
Examples:

```bash
comparer.py -i filenames_in_dir.txt -o current_filename_in_dir.txt -c ls
```
  
## Authors

* **Patrick Sukop** - *Initial work* - [Knadt](https://github.com/Knadt)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Richard - Richard - Richard
