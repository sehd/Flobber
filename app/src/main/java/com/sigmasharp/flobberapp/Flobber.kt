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
    fun start() {
        messaging.subscribe(WebServer.moveForwardRequested) { _ -> moveForwardHandler() }
        messaging.subscribe(WebServer.moveBackwardRequested) { _ -> moveBackwardHandler() }
        messaging.subscribe(WebServer.moveLeftRequested) { _ -> moveLeftHandler() }
        messaging.subscribe(WebServer.moveRightRequested) { _ -> moveRightHandler() }
        messaging.subscribe(WebServer.moveStopRequested) { _ -> stopHandler() }
    }

    private fun moveForwardHandler() {
        bluetooth.send("f")
    }

    private fun moveBackwardHandler() {
        bluetooth.send("b")
    }

    private fun moveLeftHandler() {
        bluetooth.send("l")
    }

    private fun moveRightHandler() {
        bluetooth.send("r")
    }

    private fun stopHandler() {
        bluetooth.send("s")
    }
}
