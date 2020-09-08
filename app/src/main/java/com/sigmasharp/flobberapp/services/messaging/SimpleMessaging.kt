package com.sigmasharp.flobberapp.services.messaging

import com.sigmasharp.flobberapp.services.logger.Logger
import kotlin.collections.ArrayList

class SimpleMessaging(private val logger: Logger) : Messaging {
    private val subscriptions = mutableMapOf<MessageAddress, ArrayList<(content: Any?) -> Unit>>()

    override fun publish(address: MessageAddress, content: Any?) {
        if (!subscriptions.containsKey(address))
            return
        val handlers = subscriptions[address] ?: return
        for (handler in handlers) {
            try {
                handler(content)
            } catch (ex: Exception) {
                logger.addError("Message handler thrown error: " + ex.message)
            }
        }
    }

    override fun subscribe(address: MessageAddress, handler: (content: Any?) -> Unit) {
        if (!subscriptions.containsKey(address))
            subscriptions[address] = ArrayList()

        subscriptions[address]?.add(handler)
    }
}