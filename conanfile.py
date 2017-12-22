#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class WtlConan(ConanFile):
    name = "wtl"
    version = "10.0.7336"
    generators = "cmake"
    url = "https://github.com/wi3ard/conan-wtl"
    license = "MIT"
    description = "Windows Template Library (WTL)"
    exports_sources = ["LICENSE.md"]

    def source(self):
        source_url = "https://downloads.sourceforge.net/project/wtl/WTL%2010/WTL%20{0}/WTL10_7336.zip"
        tools.get(source_url.format(self.version))

    def build(self):
        pass

    def package(self):
        self.copy(pattern="*.h", src="Include", dst="Include")

    def package_id(self):
        self.info.header_only()
