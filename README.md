# xcode-build-increment

A python script that easily increments build numbers for targets in your Xcode project

Usage:

A. Increment build number for a single file:

`python3 xcode-build-increment.py <your_info.plist>`

B. Increment build number in multiple files:

0. You may want to copy files of `xcode-build-increment` under "Tools" (for an instance) folder in your main project.
1. Please edit `incbuild.sh` file and write in names for your all `Info.plist` files containing build numbers you want to be incremented simulteneously. The paths may be relative.
2. Each time you want to increments build numbers for the project, run:

`$ ./incbuild.sh`




