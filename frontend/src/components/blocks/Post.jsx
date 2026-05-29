import { Button } from '../ui/button';
import Tag from './Tag';
import { ArrowBigUp, ArrowBigDown, Bookmark, Share2, NotepadText, Flag, GitPullRequest } from 'lucide-react';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "../ui/card"

export default function post() {
  return (
    <Card className='h-fit'>
      <CardHeader className='flex items-center lg:gap-2'>
        <img src="" alt="community pfp" />
        <CardTitle className='lg:text-sm text-white/80'>Community Name</CardTitle>
        <CardDescription>• 2 hours ago</CardDescription>
      </CardHeader>

      <CardContent>
        <p className='text-muted-foreground'>Your post content goes here</p>
      </CardContent>

      <CardContent>
        {/* Tags */}
        <ul className='flex lg:gap-1'>
          <li><Tag label='Networks' /></li>
          <li><Tag label='Protocols' /></li>
          <li><Tag label='Tutorial' /></li>
        </ul>
      </CardContent>

      <CardFooter>
        {/* author details */}
        <div className='flex lg:gap-3 w-full items-center justify-between'>
          <div className='flex lg:gap-2 items-center'>
            <div className='flex lg:gap-2'>
              <div className='flex items-center bg-accent rounded-4xl'>
                <Button size='icon-lg' variant='ghost' className='hover:text-red-500' >
                  <ArrowBigUp size={30} />
                </Button>
                <p className='lg:text-sm'>69</p>
              <Button size='icon-lg' variant='ghost' className='hover:text-purple-600' >
                  <ArrowBigDown size={20} />
                </Button>
              </div>

              <Button size='lg' variant='ghost' className='bg-accent rounded-4xl'>
                <Share2 size={20} />
                Share
              </Button>

              <Button size='icon-lg' variant='ghost' className='bg-accent rounded-4xl'>
                <Bookmark size={20} />
              </Button>

              <Button  size='icon-lg' variant='ghost' className='bg-accent rounded-4xl'>
                <NotepadText size={20} />
              </Button>

              <Button  size='icon-lg' variant='destructive' className='bg-accent rounded-4xl'>
                <Flag size={20} />
              </Button>
            </div>
          </div>

          <div>
            <Button  size='lg' variant='secondary' className='bg-accent rounded-2xl'>
              <GitPullRequest size={20} />
              Add Resource
            </Button>
          </div>
        </div>
      </CardFooter>
    </Card>
  )
}