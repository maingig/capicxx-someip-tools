from conans import ConanFile, tools

# Must first use Maven to build binaries before using this file - see README

import os

class CapicxxsomeiptoolsConan(ConanFile):
    name = "capicxx-someip-tools"
    version = "3.1.12.2"
    settings = "os", "arch"
    description = "Someip tools built with maven"
    url = "None"
    license = "None"
    author = "None"
    topics = None

    def package(self):
        self.copy("*", "bin")

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

