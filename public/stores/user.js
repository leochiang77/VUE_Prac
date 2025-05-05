import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const userJson = ref("")
  const user = computed(() => {
    try {
      let res = (userJson.value || window.localStorage.getItem("user"))
      if (res) {
        window.localStorage.setItem("user", res)
        res = JSON.parse(res)
        return res
      } else {
        throw new Error("error")
      }
    } catch (error) {
      window.localStorage.setItem("user", "")
      ElMessage.error("驗證資訊儲存失敗 !!")
      return ""
    }
  })
  function saveUser(data) {
    userJson.value = data
  }

  return { user, saveUser }
})