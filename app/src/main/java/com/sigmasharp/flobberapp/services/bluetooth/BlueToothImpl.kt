package com.sigmasharp.flobberapp.services.bluetooth

import android.bluetooth.BluetoothAdapter
import android.bluetooth.BluetoothDevice
import android.bluetooth.BluetoothSocket
import com.sigmasharp.flobberapp.Config
import com.sigmasharp.flobberapp.services.logger.Logger
import java.io.IOException
import java.io.OutputStream

class BlueToothImpl(private val logger: Logger) : BlueTooth {

    private var socket: BluetoothSocket? = null
    override fun start() {
        val bluetoothAdapter = getDevice()
        if (bluetoothAdapter == null) {
            logger.addError("No bluetooth adapter!")
            return
        }
        connect(bluetoothAdapter)
    }

    override fun send(message: String) {
        val outStream: OutputStream
        try {
            if (socket == null) {
                logger.addWarning("Sending command while connecting")
            }
            outStream =
                socket?.outputStream ?: throw Exception("How did tou lost socket in this point?")
            val msgBuffer = message.toByteArray()
            outStream.write(msgBuffer)
        } catch (e: IOException) {
            logger.addError("Bluetooth connection lost:" + e.message)
            start()
        } catch (ex: Exception) {
            logger.addError("Bluetooth send error: " + ex.message)
        }
    }

    private fun getDevice(): BluetoothAdapter? {
        val bluetoothAdapter = BluetoothAdapter.getDefaultAdapter()

        if (!bluetoothAdapter.enable()) {
            logger.addError("Bluetooth disabled")
            return null
        }

        if (bluetoothAdapter == null) {
            logger.addError("No bluetooth device detected")
            return null
        }

        return bluetoothAdapter
    }

    private fun connect(bluetoothAdapter: BluetoothAdapter) {
        val device = getByName(bluetoothAdapter)
        if (device == null) {
            logger.addError("Device is not present or not paired")
            return
        }
        bluetoothAdapter.cancelDiscovery()
        try {
            socket = device.createRfcommSocketToServiceRecord(device.uuids[0].uuid)
            socket?.connect()
            if (socket?.isConnected == true)
                logger.addNormal("Bluetooth connected")
            else {
                logger.addWarning("Connection failed. Reconnecting")
                Thread.sleep(5000)
                connect(bluetoothAdapter)
            }
        } catch (e: IOException) {
            try {
                socket?.close()
            } catch (e2: IOException) {
                logger.addError("Couldn't close connection")
            }

            logger.addWarning("Connection failed. Reconnecting")
            Thread.sleep(5000)
            connect(bluetoothAdapter)
        } catch (ex: Exception) {
            logger.addError("Bluetooth failed: " + ex.message)
        }

        //TODO beginListenForData()
    }

    private fun getByName(bluetoothAdapter: BluetoothAdapter): BluetoothDevice? {
        for (device in bluetoothAdapter.bondedDevices) {
            if (device.name == Config.btTargetDeviceName)
                return device
        }
        return null
    }
}