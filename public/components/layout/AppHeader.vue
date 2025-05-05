<script setup>
import { isCollapse } from '@/components/layout/isCollapse.js'
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()
import { useRouter } from 'vue-router'
const router = useRouter()

const handleLogout = () => {
  userStore.saveUser('')
  ElMessage.success('用戶已成功登出!!')
  router.push({ name: 'login' })
}
</script>
<template>
  <el-header>
    <el-icon :size="25" @click="isCollapse = !isCollapse">
      <IEpExpand v-show="isCollapse" />
      <IEpFold v-show="!isCollapse" />
    </el-icon>

    <el-breadcrumb>
      <el-breadcrumb-item v-for="(item, index) in $route.matched" :to="{ path: item.path }">{{ item.meta.title }}</el-breadcrumb-item>
    </el-breadcrumb>

    <el-dropdown>
      <span class="el-dropdown-link">
        {{ userStore.user.name }}
        <el-icon class="el-icon--right">
          <IEpArrowDown />
        </el-icon>
      </span>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item>設置</el-dropdown-item>
          <el-dropdown-item @click="handleLogout">退出</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </el-header>
</template>
<style scoped>
.el-header {
  display: flex;
  align-items: center;
  background-color: #607d8b;
}
.el-icon {
  margin-right: 15px;
  color: #dee1e6;
}
.el-dropdown {
  margin-left: auto;
  .el-dropdown-link {
    display: flex;
    align-items: center;
    color: #dee1e6;
    cursor: pointer;
  }
}

.el-breadcrumb :deep(.el-breadcrumb__inner) {
  color: #dee1e6;
}
</style>