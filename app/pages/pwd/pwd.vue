<template>
    <view class="content">
 
		<view class="input-row">
			<text class="title">手机号：</text>
			<m-input type="text" focus clearable v-model="phone" placeholder="请输入手机号"></m-input>
		</view>
		<view class="input-row">
			<text class="title">工号：</text>
			<m-input type="text" focus clearable v-model="staffID" placeholder="请输入工号"></m-input>
		</view>

        <view class="btn-row">
            <button type="primary" class="primary" @tap="findPassword">提交</button>
        </view>
    </view>
</template>

<script>
	var  r=/^1[3|4|5|8][0-9]\d{4,8}$/;
    import service from '../../service.js';
    import mInput from '../../component/m-input.vue';

    export default {
        components: {
            mInput
        },
        data() {
            return {
                phone: '',
				staffID: '',
            }
        },
        methods: {
            findPassword:function() {
                if (!r.test(this.phone)|| this.staffID=='') {//查找数据库中对应的手机号和工号
                    uni.showToast({
                        icon: 'none',
                        title: '手机号或工号不合法',
                    });
                }
                else{
					uni.request({
						url:'http://182.92.239.229/checkinformation',
						data:{
							staffID:this.staffID,
							telephone:this.phone
						},
						success: (res) => {
							if(res.data=='True'){
								uni.navigateTo({
									url:'../confirmpwd/confirmpwd?phone='+this.phone+'&staffID='+this.staffID
								})
							}
							else{
								uni.showToast({
								    icon: 'none',
								    title: '没有此手机号或者工号错误',
								});
							}
						}
					});

				}
            }
        }
    }
</script>

<style>
	.input-row{
		margin: 30rpx;
	}
	.btn-row{
		margin: 30rpx;
	}

</style>
