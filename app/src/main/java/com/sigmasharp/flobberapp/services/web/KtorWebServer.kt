package com.sigmasharp.flobberapp.services.web

import com.sigmasharp.flobberapp.services.logger.Logger
import com.sigmasharp.flobberapp.services.messaging.MessageAddress
import com.sigmasharp.flobberapp.services.messaging.Messaging
import io.ktor.application.call
import io.ktor.http.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.embeddedServer
import io.ktor.server.netty.Netty

class KtorWebServer(
    private val logger: Logger,
    private val messaging: Messaging
) : WebServer {

    override fun start(port: Int) {
        embeddedServer(Netty, port) {
            routing {
                get("/") {
                    call.respondText("Hello, world!", ContentType.Text.Html)
                }
                post("move/{direction}") {
                    handleMove(call.parameters["direction"])
                    call.respond(HttpStatusCode.OK)
                }
            }
        }.start(false)
    }

    private fun handleMove(direction: String?) {
        when (direction) {
            "f" -> messaging.publish(WebServer.moveForwardRequested)
            "b" -> messaging.publish(WebServer.moveBackwardRequested)
            "l" -> messaging.publish(WebServer.moveLeftRequested)
            "r" -> messaging.publish(WebServer.moveRightRequested)
            "s" -> messaging.publish(WebServer.moveStopRequested)
            else -> logger.addWarning("Unknown move command issued: $direction")
        }
    }
}