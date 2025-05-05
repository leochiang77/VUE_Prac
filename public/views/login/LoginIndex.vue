<script setup>
import { login } from '@/api/login'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { get_emp_data_fb_userid } from '@/composables/useEmp'
const userStore = useUserStore()
const router = useRouter()
const route = useRoute()

const isLoading = ref(false)
const form = reactive({
  account: '',
  password: '',
})

const ruleFormRef = ref()
const rules = reactive({
  account: [{ required: true, message: '請輸入帳號', trigger: 'blur' }],
  password: [
    { required: true, message: '請輸入密碼', trigger: 'blur' },
    //{ min: 6, max: 10, message: '密碼長度6~10位', trigger: 'blur' },
  ],
})

const submitForm = async (formEl) => {
  isLoading.value = true
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (!valid) {
      isLoading.value = false
      ElMessage.error('登入驗證失敗!')
      throw new Error('登入驗證失敗!', fields)
    }
  })
  const data = await login(form).then((res) => {
    if (res.data.Validity_Type == 'success') {
      return res.data
    } else {
      isLoading.value = false
      ElMessage.error(res.data.Validity_Title)
      throw new Error(res.data.Validity_MSG)
    }
  })

  if (data) {
    let authLevel = ''
    let domainLevel = ''
    let empInfo = await get_emp_data_fb_userid(data.User_Info['deptno'], data.User_Info['userid'])
    if (empInfo) {
      authLevel = empInfo['AUTH_LEVEL']
      domainLevel = empInfo['DOMAIN_LEVEL']
    }
    data.User_Info['AUTH_LEVEL'] = authLevel
    data.User_Info['DOMAIN_LEVEL'] = domainLevel
  }
  //console.log(data)
  isLoading.value = false
  ElMessage.success(data.Validity_Title)
  userStore.saveUser(JSON.stringify(data.User_Info))
  router.push(route.query.redirect || '/')
}
</script>
<template>
  <div class="login">
    <el-form ref="ruleFormRef" :model="form" label-width="auto" style="max-width: 600px" size="large" label-position="top" :rules="rules">
      <h3>登入</h3>
      <el-form-item label="帳號" prop="account">
        <el-input v-model="form.account" />
      </el-form-item>
      <el-form-item label="密碼" prop="password">
        <el-input type="password" v-model="form.password" show-password />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm(ruleFormRef)" :loading="isLoading">Login</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<style scoped>
.login {
  height: 100vh;
  background-color: rgb(214, 197, 197);
  display: flex;
  justify-content: center;
  align-items: center;
}

.el-form {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  width: 300px;
  margin-top: -100px;
}

.el-form-item {
  margin-top: 20px;
  .el-button {
    width: 100%;
  }
}
</style>