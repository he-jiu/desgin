<template>
	<view class="content">
	    <view class="input-group">
	        <view class="input-row border">
	            <text class="title border">手机号：</text>
	            <m-input class="m-input" type="text" clearable focus v-model="account" placeholder="请输入手机号"></m-input>
	        </view>
	        <view class="input-row border">
	            <text class="title border">密码：</text>
	            <m-input type="password" displayable v-model="password" placeholder="请输入密码"></m-input>
	        </view>
	    </view>
	    <view class="btn-row">
	        <button type="primary" class="login" @tap="bindLogin">登录</button>
	    </view>
	    <view class="action-row">
			<navigator url="../pwd/pwd">忘记密码</navigator>
	    </view>
	</view>
</template>

<script>
	var  r=/^1[3|4|5|8][0-9]\d{4,8}$/;
	import service from '../../service.js';
	import {
	    mapState,
	    mapMutations
	} from 'vuex'
	import mInput from '../../component/m-input.vue'
	
	export default {
		components: {
			mInput
		},
		data() {
			return {
			    account: '',
			    password: '',
			  
			}
		},
		onLoad() {

		},
		methods: {
			bindLogin:function(){
				if(r.test(this.account) && this.password){
					//获取数据name number usertype
					 uni.request({
					 	
					 	url:'http://182.92.239.229/checklogin',
					 	data:{
							telephone:this.account,
							password:this.password
						},
					 
					 	success: (res) => {
					 		console.log(res.data);
							if(res.data=='False'){
								uni.showToast({
									icon:'none',
									title:'手机号或密码错误'
								})
							}
							else{
								uni.setStorageSync('name', res.data.name);
								uni.setStorageSync('number', res.data._id);
								uni.setStorageSync('usertype',res.data.staffKind);
								uni.switchTab({ url: '../user/user' })
							}
					 	}
					 });
						
				}
					
				else{
					uni.showToast({
						icon:'none',
						title:"手机号或密码不合法"
					})
				}
			}
			
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction:column;
		align-items:center;
		justify-content: center;
		margin-top: 200rpx;
	}

	.login{
		width: 500rpx;
	}
	
	.title {
		font-size: 36rpx;
		color: #000000;
	}
	.btn-row{
		margin-top: 100rpx;
	}
	.input-row{
		margin-top: 20rpx;
	}
</style>
