-- Smart enter: navigate into directories, open files
return {
	entry = function()
		local h = cx.active.current.hovered
		if h and h.cha.is_dir then
			ya.manager_emit("enter", {})
		else
			ya.manager_emit("open", {})
		end
	end,
}
