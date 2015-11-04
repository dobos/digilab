{
 "metadata": {
  "name": "Untitled0"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "import serial\n",
      "import array"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 84
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "port = \"/dev/ttyUSB0\"\n",
      "ser = serial.Serial(port, 1200, timeout=3)\n",
      "print(ser)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "Serial<id=0x7173e310, open=True>(port='/dev/ttyUSB0', baudrate=1200, bytesize=8, parity='N', stopbits=1, timeout=3, xonxoff=False, rtscts=False, dsrdtr=False)\n"
       ]
      }
     ],
     "prompt_number": 317
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def send(data):\n",
      "    bb = array.array('B', data).tostring()\n",
      "    ser.write(bb)\n",
      "    ser.flush()\n",
      "    return ser.read(ser.inWaiting())"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 247
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def init():\n",
      "    return send([0x20, 0x15, 0xF1, 0xF2, 0xF3, 0x03])\n",
      "def move():\n",
      "    return send([0x20, 0x01, 0x55, 0x03])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "init()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 260,
       "text": [
        "b''"
       ]
      }
     ],
     "prompt_number": 260
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "send([0x03])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 313,
       "text": [
        "b''"
       ]
      }
     ],
     "prompt_number": 313
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ser.close()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ser.read(ser.inWaiting())"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 323,
       "text": [
        "b''"
       ]
      }
     ],
     "prompt_number": 323
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "send([0x03])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "pyout",
       "prompt_number": 331,
       "text": [
        "b''"
       ]
      }
     ],
     "prompt_number": 331
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}