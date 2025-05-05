<script setup>
import AppAside from '@/components/layout/AppAside.vue'
import AppHeader from '@/components/layout/AppHeader.vue'
</script>
<template>
  <div class="common-layout">
    <el-container>
      <AppAside></AppAside>
      <el-container class="containerFormat">
        <AppHeader></AppHeader>

        <el-main>
          <el-scrollbar>
            <RouterView />
          </el-scrollbar>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<style scoped>
.containerFormat {
  flex-direction: column;
  height: 100vh;
}
.el-main {
  padding-right: 0;
}
</style>