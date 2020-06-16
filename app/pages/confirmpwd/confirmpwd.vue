<template>
	<view class="content">
		<view class="input-group">
			<view class="input-row border">
				<text class="title border">请输入密码</text>
				 <m-input class="password" type="password" displayable v-model="password1" placeholder="密码"></m-input>
			</view>
		</view>
		<view class="input-group">
			<view class="input-row border">
				<text class="title border">请确认密码</text>
				 <m-input class="password" type="password" displayable v-model="password2" placeholder="密码"></m-input>
			</view>
		</view>
		<view class="btn-row">
		    <button type="primary" class="primary" @tap="confirmPassword">确认</button>
		</view>
	</view>
</template>

<script>
	import mInput from '../../component/m-input.vue'
	import service from '../../service.js';
	import {
	    mapState,
	    mapMutations
	} from 'vuex'
	export default {
		components: {
			mInput
		},
		data() {
			return {
			  password1:'',
			  password2:'',
			  staffID:'',
			}
		},
		onLoad() {
	
		},
		methods: {
			onLoad:function(option){
				console.log(option);
				this.staffID=option.staffID;

			},
			
			confirmPassword:function() {
			    
			    if (this.password1 != this.password2 ) {
			        uni.showToast({
			            icon: 'none',
			            title: '两次密码不一致',
			        });
			        return;
			    }
				else if (this.password1 == '') {
				    uni.showToast({
				        icon: 'none',
				        title: '密码不能为空',
				    });
				    return;
				}
			    else {
					uni.request({//上传数据库  this.staffid this.password
						url:'http://182.92.239.229/changepassword',
						data:{
							staffID:this.staffID,
							password:this.password1
						},
						success: (res) => {
							console.log(res.data);
						}
					})

					
					uni.showToast({
						icon: 'none',
						title: '修改密码成功',
						duration: 3000,
						
					});


					setTimeout(function() {
						uni.reLaunch({
							url:'../login/login'
						})
							},1000);
					
				
				
				}
			}
		}
	}
	
</script>

<style>
	.input-group{
		margin: 20rpx;
	}
	.btn-row{
		margin: 20rpx;
	}
	.password{
		margin-top: 10rpx;
		border: 1rpx;
		border-color: #000000;
	}
</style>
