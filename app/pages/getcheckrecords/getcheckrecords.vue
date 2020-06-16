<template>
	<view>
		<view class="input">
			输入用户id
			<input v-model='ID' placeholder="输入用户ID" />
		</view>

		<view class="input">
			<view>
				选择日期
				<view class="">
					<picker mode="date" :value="date"  @change="bindDateChange">
						<view class="">{{date}}</view>
					</picker>
				</view>
			</view>
		</view>
		<view>
			<button @click="submit" type="primary" v-show="buttonTag">提交</button>
		</view>
		<view v-show="textTag" class="content">
			<view>
				<view class="text">管道: <view>{{array[tube]}}</view></view>
				<view class="text">阀门: <view>{{array[valve]}}</view></view>
				<view class="text">设备: <view>{{array[device]}}</view></view>
				<view class="text">备注: <view>{{remark}}</view></view>
			</view>
			<view>
				照片：
				<image :src='src'></image>
			</view>
			
		</view>
		<view>
			<button @click="refresh" type="primary" v-show="returntag">返回</button>
		</view>
	</view>

</template>

<script>
	export default {
			data() {
				const currentDate = this.getDate({
					format: true
				})
				return {
					array:[' ','良好','一般','需要更换'],
					date: currentDate,
					buttonTag:true,
					returntag:false,
					textTag:false,
					tube:'',
					valve:'',
					device:'',
					remark:'',
					src:'',
					ID:''
				}
			},
			methods: {
				bindDateChange: function(e) {
					this.date = e.target.value
				},
				
				getDate(type) {
					const date = new Date();
					let year = date.getFullYear();
					let month = date.getMonth() + 1;
					let day = date.getDate();
	 
					if (type === 'start') {
						year = year - 60;
					} else if (type === 'end') {
						year = year + 2;
					}
					month = month > 9 ? month : '0' + month;;
					day = day > 9 ? day : '0' + day;
					return `${year}-${month}-${day}`;
				},
				
				submit:function(){
					uni.request({
						url:'http://182.92.239.229/getcheckrecords',
						data:{
							id:this.ID,
							date:this.date
						},
						success: (res) => {
							if(res.data==false){
								uni.showToast({
									icon:'none',
									title:'没有该用户或者该日期没有检测记录'
								})
							}
							else{
								this.buttonTag=false,
								this.textTag=true,
								this.returntag=true,
								this.tube=res.data.tube,
								this.valve=res.data.valve,
								this.device=res.data.device,
								this.remark=res.data.remarks,
								this.src='http://182.92.239.229/'+res.data.imgurl
							}
							
						}
					})
				},
				
				refresh:function(){
					uni.redirectTo({
						url:'../getcheckrecords/getcheckrecords'
					})
				}
			}
		}
</script>

<style>
	.input{
		margin: 20rpx;
	}
	.text{
		display: flex;
		margin: 20rpx;
	}
</style>
