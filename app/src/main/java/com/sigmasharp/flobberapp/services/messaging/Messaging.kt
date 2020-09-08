package com.sigmasharp.flobberapp.services.messaging

interface Messaging {
    fun publish(address: MessageAddress, content: Any? = null)
    fun subscribe(address: MessageAddress, handler: (content: Any?) -> Unit)
}