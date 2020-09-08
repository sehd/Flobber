package com.sigmasharp.flobberapp.services.messaging

class SimpleMessaging : Messaging {
    override fun publish(address: MessageAddress, content: Any?) {
        TODO("Not yet implemented")
    }

    override fun subscribe(address: MessageAddress, handler: (content: Any?) -> Unit) {
        TODO("Not yet implemented")
    }
}