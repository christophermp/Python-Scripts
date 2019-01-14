#!/usr/bin/env python
# encoding: utf-8

import npyscreen

def simple_function( *arguments ):
    form = npyscreen.Form( name = 'npyscreen Form!')
    form.edit()

if ( __name__ == "__main__" ):
    npyscreen.wrapper_basic( simple_function )
    