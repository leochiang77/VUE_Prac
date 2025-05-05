<script setup>
import { isCollapse } from '@/components/layout/isCollapse.js'
</script>
<template>
  <el-aside width="200px">
    <el-scrollbar>
      <el-menu :collapse="isCollapse" router>
        <a href="/" class="logo">
          <!-- <img src="@/assets/logo.svg" /> -->
          <h1>Domain</h1></a
        >
        <el-sub-menu index="1">
          <template #title>
            <el-icon><IEpUserFilled /></el-icon>
            <span>人才管理</span>
          </template>
          <el-menu-item index="statistic">
            <el-icon><IEpTrendCharts /></el-icon>統計報表
          </el-menu-item>
          <el-menu-item index="pplskill">
            <el-icon><IEpTrendCharts /></el-icon>個人專業能力
          </el-menu-item>
          <el-menu-item index="explain">
            <el-icon><IEpTrendCharts /></el-icon>認證評分說明
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="2">
          <template #title>
            <el-icon><IEpTools /></el-icon>
            <span>系統連結</span>
          </template>
          <el-menu-item><a type="link" href="http://tw100043771.corpnet.auo.com:5100/UAC.asp" target="_blank">技師技能盤點</a></el-menu-item>
          <el-menu-item><a type="link" href="http://tw100039807.corpnet.auo.com/LCD2IMS/Dashboard" target="_blank">工程師技能盤點</a></el-menu-item>
        </el-sub-menu>
      </el-menu>
    </el-scrollbar>
  </el-aside>
</template>
<style scoped>
.el-aside {
  background-color: #eee;
  height: 100vh;
  width: auto;
}
.el-menu {
  width: 200px;
  background-color: #eee;
  border-right: none;
  &.el-menu--collapse {
    width: 60px;
    & h1 {
      display: none;
    }
  }
}

.logo {
  display: flex;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  height: 60px;
  & img {
    width: 32px;
    height: 32px;
  }
}
</style>