package com.sigmasharp.flobberapp

import com.sigmasharp.flobberapp.services.bluetooth.BlueTooth
import com.sigmasharp.flobberapp.services.logger.Logger
import com.sigmasharp.flobberapp.services.messaging.Messaging
import com.sigmasharp.flobberapp.services.web.WebServer

class Flobber(
    private val logger: Logger,
    private val messaging: Messaging,
    private val bluetooth: BlueTooth
) {
    private var moving = false

    fun start() {
        moving = false
        messaging.subscribe(WebServer.moveForwardRequested) { _ -> moveForwardHandler() }
        messaging.subscribe(WebServer.moveBackwardRequested) { _ -> moveBackwardHandler() }
        messaging.subscribe(WebServer.moveLeftRequested) { _ -> moveLeftHandler() }
        messaging.subscribe(WebServer.moveRightRequested) { _ -> moveRightHandler() }
        messaging.subscribe(WebServer.moveStopRequested) { _ -> stopHandler() }
    }

    private fun moveForwardHandler() {
        if (moving) {
            bluetooth.send("s")
            Thread.sleep(500)
        }
        bluetooth.send("f")
        moving = true
    }

    private fun moveBackwardHandler() {
        if (moving) {
            bluetooth.send("s")
            Thread.sleep(500)
        }
        bluetooth.send("b")
        moving = true
    }

    private fun moveLeftHandler() {
        if (moving) {
            bluetooth.send("s")
            Thread.sleep(500)
        }
        bluetooth.send("l")
        moving = true
    }

    private fun moveRightHandler() {
        if (moving) {
            bluetooth.send("s")
            Thread.sleep(500)
        }
        bluetooth.send("r")
        moving = true
    }

    private fun stopHandler() {
        bluetooth.send("s")
        moving = false
    }
}
