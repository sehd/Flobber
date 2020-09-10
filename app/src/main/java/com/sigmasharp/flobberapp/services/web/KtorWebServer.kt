package com.sigmasharp.flobberapp.services.web

import android.content.Context
import android.content.res.AssetManager
import android.net.wifi.WifiManager
import androidx.core.content.getSystemService
import com.sigmasharp.flobberapp.services.logger.Logger
import com.sigmasharp.flobberapp.services.messaging.Messaging
import io.ktor.application.*
import io.ktor.http.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*


class KtorWebServer(
    private val logger: Logger,
    private val messaging: Messaging,
    private val assets: AssetManager
) : WebServer {

    override fun start(port: Int, context: Context) {
        val html = assets.open("index.html").bufferedReader()
            .use {
                it.readText()
            }
        embeddedServer(Netty, port) {
            routing {
                get("/") {
                    call.respondText(html, ContentType.Text.Html)
                }
                post("move/{direction}") {
                    handleMove(call.parameters["direction"])
                    call.respond(HttpStatusCode.OK)
                }
            }
        }.start(false)
        try {
            reportWifiState(port, context)
        } catch (ex: Exception) {
            logger.addError("Server started but couldn't print wifi state: " + ex.message)
        }
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

    private fun reportWifiState(port: Int, context: Context) {
        context.getSystemService<WifiManager>().let {
            when {
                it == null -> logger.addWarning("No wifi available")
                !it.isWifiEnabled -> logger.addWarning("Wifi is disabled")
                it.connectionInfo == null -> logger.addWarning("Wifi not connected")
                else -> {
                    val ip = it.connectionInfo.ipAddress
                    val ipStr = ((ip and 0xFF).toString() + "." +
                            (ip shr 8 and 0xFF) + "." +
                            (ip shr 16 and 0xFF) + "." +
                            (ip shr 24 and 0xFF))
                    logger.addNormal("Server started at -> $ipStr:$port")
                }
            }
        }
    }
}