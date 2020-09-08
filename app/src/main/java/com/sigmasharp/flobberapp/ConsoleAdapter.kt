package com.sigmasharp.flobberapp

import android.graphics.Color
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.sigmasharp.flobberapp.services.console.ConsoleItem
import com.sigmasharp.flobberapp.services.console.ConsoleItemType
import kotlinx.android.synthetic.main.console_item_row.view.*

class ConsoleAdapter(private val items: ArrayList<ConsoleItem>) :
    RecyclerView.Adapter<ConsoleAdapter.ConsoleItemHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ConsoleAdapter.ConsoleItemHolder {
        val inflatedView = parent.inflate(R.layout.console_item_row, false)
        return ConsoleItemHolder(inflatedView)
    }

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(holder: ConsoleAdapter.ConsoleItemHolder, position: Int) {
        holder.bindItem(items[position])
    }

    class ConsoleItemHolder(v: View) : RecyclerView.ViewHolder(v) {
        private var view: View = v

        fun bindItem(item:ConsoleItem){
            view.consoleItem.text = item.Content
            when (item.Type) {
                ConsoleItemType.Normal -> view.consoleItem.setTextColor(
                    Color.parseColor("#ff99cc00"))
                ConsoleItemType.Warning -> view.consoleItem.setTextColor(
                    Color.parseColor("#ffffbb33"))
                ConsoleItemType.Error -> view.consoleItem.setTextColor(
                    Color.parseColor("#ffff4444"))
            }
        }
    }

}
